const solution = (arr,divisor) => {
    const as = [];
    for (el of arr) if(!(el%divisor)) as.push(el); 
    
    return as.length ? as.sort((a,b)=>a-b) : [-1];
}