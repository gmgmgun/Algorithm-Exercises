function solution(n) {
    var tern = [];
    
    while (n >= 1) {
        tern.push(n%3);
        n = parseInt(n/3);
    }
    
    return tern.reverse().reduce((acc,cur,idx) => acc += cur * 3 ** idx);
}