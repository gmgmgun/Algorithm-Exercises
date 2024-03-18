let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');

const count = Number(input[0]);
const arr =  [];

for (let i = 1; i <= count; i++) {
  const el = Number(input[i]);

  if(el) {
    arr.push(el);
  } else {
    arr.pop();
  }
}

let result = arr.reduce((acc,cur) => acc + cur, 0);
console.log(result);