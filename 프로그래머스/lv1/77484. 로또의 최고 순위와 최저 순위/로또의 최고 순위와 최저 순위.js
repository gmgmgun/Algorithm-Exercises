function getRank(num) {
    if(!num) return 6;
    else return 7-num;
}

function solution(lottos, win_nums) {
    var answer = [];
    let cntCorrect = 0;
    let cntZero = lottos.filter(element => 0 === element).length;
    
    for(let i = 0; i < win_nums.length; i++) {
        if (win_nums.indexOf(lottos[i]) !== -1) {
            cntCorrect++;
        } 
    }
    
    answer.push(getRank(cntCorrect+cntZero));
    answer.push(getRank(cntCorrect));
    
    return answer;
}