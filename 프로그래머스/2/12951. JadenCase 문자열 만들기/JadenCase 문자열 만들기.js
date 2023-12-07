const solution = s => {
    const arr = s.split(' ').map((el)=> {
        return toJadenCase(el);
    })
    
    return arr.join(' ');
}

const toJadenCase = str => {
    const arr = str.split('').map((el,idx)=>{
        if(idx) return el.toLowerCase();
        else return el.toUpperCase();  
    })
    
    return arr.join('');
}