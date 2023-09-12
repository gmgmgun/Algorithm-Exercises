const solution = (arr) => {
    var answer = [];
    
    for (el of arr) {
        if(answer[answer.length-1] !== el) answer.push(el)
    }
    
    return answer;
}