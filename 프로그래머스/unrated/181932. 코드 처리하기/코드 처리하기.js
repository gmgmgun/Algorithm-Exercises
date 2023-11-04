const solution = (code) => {
    let mode = 0;
    let ret = '';
    
    for (let i = 0; i < code.length; i++) {
        if (mode) {
            if (code[i] === "1") {
                mode = 0;
            } else {
                if(i%2) ret += code[i];
            }
        } else {
            if (code[i] === "1") {
                mode = 1;
            } else {
                if(!(i%2)) ret += code[i];
            }
        }
    }
    
    return ret ? ret : "EMPTY";
}