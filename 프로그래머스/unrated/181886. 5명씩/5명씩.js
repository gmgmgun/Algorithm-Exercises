function solution(names) {
    var answer = [];
    let idx = 0;
    
    names.forEach(name=>{
        if(idx%5 === 0) answer.push(name);
        idx++;
    })
    
    return answer;
}