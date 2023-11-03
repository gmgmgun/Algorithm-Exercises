const solution = (n) => {    
    let sum = 0;
    
    if (n%2) {
        while(n >= 0) {
            sum += n;
            n = n-2;
        }
    }
    
    if (!(n%2)) {
        while(n >= 0) {
            sum += n*n;
            n = n-2;
        }
    }
    
    return sum;
}