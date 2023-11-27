function solution(s,e) {
    const arr = [];
    
    do {
        arr.push(s);
        s--;
    } while(s >= e);
    
    return arr;
}