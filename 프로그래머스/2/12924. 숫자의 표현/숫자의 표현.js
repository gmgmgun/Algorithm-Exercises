function solution(n) {
    let answer = 0;
    
    for(let i = 1; i <= n; i++) {
        if(foo(n,i)) answer++;
    }
    
    return answer;
}

function foo(num,start) {
    let cnt = 0;
    for(let i = start; i <= num; i++) {
        cnt += i;
        if(num === cnt) return true;
        if(cnt > num) return false;
    }
    return false;
}