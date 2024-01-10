function solution(rsp) {
    let answer = '';
    
    rsp.split('').forEach(el=> {
        if (el === '2') answer += '0';
        if (el === '0') answer += '5';
        if (el === '5') answer += '2';
    })
    
    return answer;
}