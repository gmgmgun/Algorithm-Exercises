function solution(k, m, score) {
    var answer = 0;
    let obj = {};
    let reminder = 0;
    let apples = score.map(
        (el)=> { if(obj[el]) obj[el]++
                 else obj[el] = 1 }
    );
    
    for (let i = 9; i >= 0; i--) {
        if(obj[i]) {
            obj[i] += reminder;
            answer += parseInt(obj[i]/m) * m * i;
            reminder = obj[i]%m;
        }
    }
    
    return answer;
}