function solution(cipher, code) {
    var answer = '';
    
    cipher.split('').forEach((el,idx) => {
        if((idx+1)%code === 0) answer+=el;
    });
    
    return answer;
}