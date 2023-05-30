function solution(name, yearning, photo) {
    var answer = [];
    const scoreMap = {};
    
    for(let i = 0; i < name.length; i++) {
        scoreMap[name[i]] = yearning[i];
    }
    
    for(let i = 0; i < photo.length; i++) {
        let sum = 0;
        for(let j = 0; j < photo[i].length; j++) {
            if(scoreMap[photo[i][j]] > 0) {
                sum += scoreMap[photo[i][j]]; 
            }
        }
        answer.push(sum);
    }
    return answer;
}