function solution(strings, n) {
    strings.sort((a,b)=> {
        if(a[n].charCodeAt()>b[n].charCodeAt()) return 1;
        if(a[n].charCodeAt()<b[n].charCodeAt()) return -1;
        if(a[n].charCodeAt() === b[n].charCodeAt()) {
            for (let i = 0; i < a.length; i++) {    
                if(a[i].charCodeAt()>b[i].charCodeAt()) return 1;
                if(a[i].charCodeAt()<b[i].charCodeAt()) return -1;
            }
        }
    })
    return strings;
}