function solution(x) {
    var sum = 0;
    var digit = x.toString().split('').forEach(el => sum += Number(el));
    
    if(x%sum) return false;
    
    return true;
}