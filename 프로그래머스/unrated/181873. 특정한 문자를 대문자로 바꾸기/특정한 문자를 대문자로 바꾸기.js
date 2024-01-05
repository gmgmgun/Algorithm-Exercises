const solution = (str,alp) => str.split('').map(el => {
    if(el === alp) return el.toUpperCase();
    return el;
}).join('');