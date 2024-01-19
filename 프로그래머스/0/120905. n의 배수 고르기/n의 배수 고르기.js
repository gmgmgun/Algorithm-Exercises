function solution(n, numlist){
    const answer = [];
  
    numlist.forEach(el => {
        if(el%n===0) answer.push(el);
    });
    
    return answer;
}