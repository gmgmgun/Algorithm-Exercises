function solution(n) {
    var answer = [];
    for (let i = n; i >=1; i-- ) {
        if(i%2) answer.push(i);
    }
    return answer.sort((a,b)=>a-b);
}