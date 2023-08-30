function solution(left, right) {
    var answer = 0;
    
    for(let i = left; i <= right; i++) {
        if (i === 1) {
            answer = - 1;
        } else {
            let cnt = 2;
        
            for(let j = 2; j <= i/2; j++) {
                if(i%j === 0) cnt++;
            }
            cnt % 2 ===0 ? answer += i : answer -= i;   
        }
    }
    
    return answer;
}