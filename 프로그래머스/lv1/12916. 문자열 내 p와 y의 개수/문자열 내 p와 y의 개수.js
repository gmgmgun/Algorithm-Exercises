function solution(s){
    s = s.toLowerCase().split('');
    let arr = Array(2).fill(0);
    
    for (el of s) {
        if (el === 'p') arr[0]++;
        if (el === 'y') arr[1]++;
    }
    
    if (arr[0] === arr[1]) return true;
    return false;
}