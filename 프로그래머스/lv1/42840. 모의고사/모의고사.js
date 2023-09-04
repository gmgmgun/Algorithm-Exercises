function solution(answers) {
    let correct = Array(3).fill(0);
    
    for (idx in answers) {
        idx = parseInt(idx);  
        if(answers[idx] === supo1(idx)) correct[0]++;
        if(answers[idx] === supo2(idx)) correct[1]++;
        if(answers[idx] === supo3(idx)) correct[2]++;
    }
    
    let answer = correct.map((el,idx) => el === Math.max(...correct) ? el = idx+1 : el = -1 ).filter(el=> el > 0).sort((a,b)=>a-b);
    
    return answer;
}

const supo1 = (idx) => {
    return (idx)%5+1
}

const supo2 = (idx) => {
    if (idx%2 === 0) return 2;
    else {
        if (idx%8 === 1) return 1;
        if (idx%8 === 3) return 3;
        if (idx%8 === 5) return 4;
        if (idx%8 === 7) return 5;
    }
}

const supo3 = (idx) => {
    if (Math.floor(idx/2)%5 === 0) return 3;
    if (Math.floor(idx/2)%5 === 1) return 1;
    if (Math.floor(idx/2)%5 === 2) return 2;
    if (Math.floor(idx/2)%5 === 3) return 4;
    if (Math.floor(idx/2)%5 === 4) return 5;
}