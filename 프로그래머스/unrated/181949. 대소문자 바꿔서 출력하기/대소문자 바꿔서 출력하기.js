const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    input = [line];
}).on('close',function(){
    str = input[0];
    
    let answer = '';
    
    for (el of str) {
      el.charCodeAt() < 97 ? answer += el.toLowerCase() : answer += el.toUpperCase() 
    }
    
    console.log(answer);
});