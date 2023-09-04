function solution(array, commands) {
    var answer = [];
    
    for (cmd of commands) {
        const [start,leng,target] = cmd;
        let el = array.slice(start-1,leng).sort((a,b)=>a-b);
        answer.push(el[target-1])
    }   
    
    return answer;
}