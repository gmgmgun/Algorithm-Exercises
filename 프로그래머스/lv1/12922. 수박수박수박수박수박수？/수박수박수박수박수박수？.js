const solution = (n) => {
    let i = 1;
    let str = '';
    
    while(i<=n) {
        i%2? str += '수' : str += '박' 
        i++;
    }
    
    return str;
}