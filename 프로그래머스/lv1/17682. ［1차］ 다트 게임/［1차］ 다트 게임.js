function solution(dartResult) {
    var answer = [];
    var res = 0;
    
    for(let i = 0; i < dartResult.length; i++) {
        if(Number.isInteger(Number(dartResult[i]))) {
            if(i) answer.push(res);
            res = Number(dartResult[i]);
        }
        else if (dartResult[i] === 'D') res **= res;
        else if (dartResult[i] === 'T') res = res*res*res;
        else if (dartResult[i] === '*') {
            res = res*2;
            if(answer[i-1]) answer[i-1] = answer[i-1]*2
        }
        else if (dartResult[i] === '#') res = res*(-1);
    }
    if (i = dartResult.length) answer.push(res);
    console.log(answer)
    const sum = answer.reduce((acc,cur) => acc+cur)
    return sum;
}