function solution(N, stages) {
    let remain = stages.length;
    let rate ={};
    
    for(let i = 1; i <= N; i++) {
        let fail = 0;
        for (user of stages) {
            if (user === i) {
                fail++;
            }
        }
        rate[i] = fail/remain;
        remain -= fail;
    }
    
    let arr = Object.entries(rate).sort((a,b) => b[1]-a[1]).map(el => Number(el[0]));
    
    return arr;
}