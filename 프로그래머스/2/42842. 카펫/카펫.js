function solution(brown, yellow) {
    let answer = [];
    const area = brown + yellow;
    const round = brown;
    
    const combs = getCombs(area); 
    
    combs.forEach((comb)=> {
       if(((comb[0] + comb[1])*2 - 4) === round) {
           answer = comb;
       }  
    })
    
    return answer;
}

function getCombs(area) {
    const combs = [];
    for(let i = 1; i<=area; i++) {
        if((area%i) === 0 && (i >= area/i)) combs.push([i,area/i]);
        
    }
    
    return combs;
}