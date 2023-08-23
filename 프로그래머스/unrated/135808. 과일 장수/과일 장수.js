function solution(k, m, score) {
    let obj = {};
    let reminder = 0;
    
    score.map((el)=> { 
                       if(obj[el]) obj[el]++
                       else obj[el] = 1 
                     });
    
    let answer = Object.keys(obj).sort((a,b)=>b-a).reduce((acc,el) =>{
        obj[el] += reminder;
        reminder = obj[el]%m;
        return acc + parseInt(obj[el]/m) * m * el; 
    },0)
    
    return answer;
}