function solution(k, score) {
    var answer = [];
    for (let i = 1; i <= score.length; i++) {
        let hof = score.slice(0,i).sort((a, b) => b - a).slice(0,k)
        answer.push(hof[hof.length-1])
    }
    return answer;
}