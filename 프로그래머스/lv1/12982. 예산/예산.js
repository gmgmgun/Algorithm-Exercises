function solution(d, budget) {
    d = d.sort((a,b) => a-b);
    
    let cnt = 0;
    
    while(1) {
        if(budget < d[cnt] || cnt === d.length) break;
        budget -= d[cnt];
        cnt++;
    }
    
    return cnt;
}