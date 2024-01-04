const solution = (arr,n) => {
    if(arr.length % 2) {
        return arr.map((el,idx)=> {
            if(idx%2 === 0) return el+n;
            return el;
        })
    }
    
    return arr.map((el,idx)=> {
            if(idx%2) return el+n;
            return el;
    })
}