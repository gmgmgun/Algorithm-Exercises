function solution(n) {
    var answer = 0;
    let num = [...String(n)];
    
    num.forEach((number)=> {
        answer += Number(number);
    })
    
    return answer;
}