function solution(n) {
    let first=0;
    let second=1;
    let target=0;
    
    for(let i=2;i<=n;i++) {
        target = (first + second)%1234567;
        
        first = second;
        second = target; 
    }

    return target;
}