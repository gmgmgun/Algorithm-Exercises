function solution(l, r) {
    var answer = [];
    
    for(let i = l; i <= r; i++) {
        if(foo(i)) answer.push(i);
    }
    
    return answer.length ? answer : [-1];
}

function foo (num) {
    let str = String(num);
    
    for (let i = 0; i < str.length; i++) {
        if(str[i] !== '5' && str[i] !== '0') return false;
    }
    
    return true;
}