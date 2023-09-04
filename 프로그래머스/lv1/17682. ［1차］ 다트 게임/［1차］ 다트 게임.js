function solution(dartResult) {
    var scores = [];
    var score = 0;
    var idx = -1;
    
    dartResult = dartResult.match(/(\d+|[^\d])/g);
    
    for(let i = 0; i < dartResult.length; i++) {
        if(Number.isInteger(Number(dartResult[i]))) {
            if(i) {
                scores.push(score);
                idx++;
            }
            score = Number(dartResult[i]);
        }
        else if (dartResult[i] === 'D') score = score**2;
        else if (dartResult[i] === 'T') score = score**3;
        else if (dartResult[i] === '*') {
            score = score*2;
            if(scores[idx]) scores[idx] = scores[idx]*2
        }
        else if (dartResult[i] === '#') score = score*(-1);
    }
    
    if (i = dartResult.length) scores.push(score);
    
    return scores.reduce((acc,cur) => acc+cur);
}