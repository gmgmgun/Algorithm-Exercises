function solution(n)
{
    var ans = 0;
    
    while(n > 0) {
        if(n%2) {
            n -= 1;
            ans++;
        }
        else n /= 2;
    }
    
    return ans;
}