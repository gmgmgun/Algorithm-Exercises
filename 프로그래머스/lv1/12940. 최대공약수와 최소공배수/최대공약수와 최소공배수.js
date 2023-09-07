function solution(n, m) {
    let i = 2;
    let divs = [];
    let min = Math.min(n,m);
    
    while(i <= min) {
        if(n%i === 0 && m%i ===0) {
            n = n/i;
            m = m/i;
            divs.push(i);
        } else i++;
    }
    
    let gongyak = divs.reduce((acc,cur) => acc*cur,1);
    let gongbae = gongyak*n*m
    
    return [gongyak,gongbae];
}