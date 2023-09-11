const solution = s => {
    s = s.split('');
    
    if (s.length !== 4 && s.length !== 6) return false;
    
    for (el of s) {
        if (!Number.isInteger(Number(el))) return false;
    }
    
    return true;
}