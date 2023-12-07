const solution = s => {
    const arr = s.split(' ');
    
    let max = 0;
    let min = 0;

    arr.forEach((el,idx)=>{
        const num = Number(el);
        if(idx === 0) {
            max = num;
            min = num;
        }
        if(num > max) max = num;
        if(num < min) min = num;
    })
    
    return `${min} ${max}`;
}