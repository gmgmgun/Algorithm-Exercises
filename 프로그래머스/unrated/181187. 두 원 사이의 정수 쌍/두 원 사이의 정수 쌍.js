const solution = (r1, r2) => {
    let sum = 0;
    
    const y = (r,x) => Math.sqrt(r**2 - x**2);
    
    const dots = x => {
        if(x < r1) {
            if (Number.isInteger(y(r1,x))) return Math.floor(y(r2,x)) - y(r1,x) + 1;
            else return Math.floor(y(r2,x)) - Math.floor(y(r1,x))
        }
        else return Math.floor(y(r2,x))+1;
    };
    
    for (let i = 1; i <= r2; i++) {
        sum += dots(i);
    }
    
    return sum*4;
}