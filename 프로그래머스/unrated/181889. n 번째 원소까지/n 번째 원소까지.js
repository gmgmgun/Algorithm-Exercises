function solution(num_list, n) {
    const answer = Array(n);
       
        for(let i=0; i<n; i++){
            answer[i]=num_list[i];
        }
        
        return answer;
}