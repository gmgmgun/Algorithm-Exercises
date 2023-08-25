function solution(a, b, n) {
    
    function getNewCoke(n,newCoke) {
        if(n < a) {
            return newCoke;
        }
        
        newCoke += parseInt(n / a) * b;
        n = parseInt(n / a) * b + n%a;
        
        return getNewCoke(n,newCoke);
    }
    
    return getNewCoke(n,0) ;
}