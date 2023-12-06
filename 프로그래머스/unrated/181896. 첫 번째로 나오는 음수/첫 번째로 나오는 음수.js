const solution = (arr) => {
    let answer = -1;
    
    arr.forEach((el,idx) => {
        if(el < 0 && answer < 0) answer = idx;
    });
    
    return answer;
}