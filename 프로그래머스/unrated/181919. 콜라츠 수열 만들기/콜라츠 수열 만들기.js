function solution(n) {
    var answer = [];
    
    while(n > 1) {
        answer.push(n);
        n%2 ? n = 3*n+1 : n = n/2
    }
    
    answer.push(1);
    
    return answer;
}