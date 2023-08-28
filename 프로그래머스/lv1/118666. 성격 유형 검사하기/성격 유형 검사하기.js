function solution(survey, choices) {
    var answer = '';
    let resMap = {};
    let arr = [['R','T'], ['C','F'], ['J','M'], ['A','N']];
    let i = 0;
    let answerArr = [];
    
    for (choice of choices) { 
        if (choice > 4) {
            if(resMap[survey[i][1]]) resMap[survey[i][1]] += Math.abs(choice-4);
            else resMap[survey[i][1]] = Math.abs(choice-4);
        } else if (choice < 4) {
            if(resMap[survey[i][0]]) resMap[survey[i][0]] += Math.abs(choice-4);
            else resMap[survey[i][0]] = Math.abs(choice-4);
        }
        i++;
    }
    
    for (res in resMap) {
        for (let i = 0; i < arr.length; i++) {
            if (arr[i].indexOf(res) !== -1 && answer.indexOf(arr[i][0]) === -1 && answer.indexOf(arr[i][1]) === -1) {
                if (resMap[arr[i][0]] >= resMap[arr[i][1]] || !resMap[arr[i][1]]) answer += arr[i][0]
                else answer += arr[i][1];
            }    
        }
    }
    
    for (el of arr) {
        if(answer.indexOf(el[0]) === -1 && answer.indexOf(el[1]) === -1) answer += el[0]
    }
    
    for (let i = 0; i < arr.length; i++) {
        for (let j = 0; j < answer.length; j++){
          if(arr[i].indexOf(answer[j]) !== -1) answerArr[i] = answer[j];   
        } 
    }
    
    
    return answerArr.join('');
}