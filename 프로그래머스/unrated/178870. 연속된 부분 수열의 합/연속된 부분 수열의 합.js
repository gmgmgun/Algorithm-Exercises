function solution(sequence, k) {
    let start = 0, end = 0;
    let sum = sequence[start];
    let answer = [];
    
    while (end <= sequence.length-1){
        if(sum < k) {
            end++;
            sum += sequence[end];
        } else if (sum > k) {
            sum -= sequence[start]
            start++;
        } else if (sum === k) {
            if(!answer.length) answer = [start,end];
            else {
                if(answer[1] - answer[0] > end - start) answer = [start,end];  
            }
            if(start===end) {
                end++;
                sum += sequence[end];
            }
            sum -= sequence[start]
            start++;
        }
    }
    
    return answer;
}