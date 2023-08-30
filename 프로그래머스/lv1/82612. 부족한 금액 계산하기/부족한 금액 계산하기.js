function solution(price, money, count) {
    var answer = money - (price * (1+count) * count/2)
   
    if(answer > 0) return 0;
    
    return Math.abs(answer);
}