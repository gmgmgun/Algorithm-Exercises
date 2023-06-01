function solution(wallpaper) {
    var answer = [];
    let luy,lux;
    let rdy = 0;
    let rdx = 0;
    
    for(let i=0; i<wallpaper.length; i++) {
        for(let j=0; j<wallpaper[0].length; j++) {
         if (wallpaper[i][j] !== "#") continue;  
         if(luy === undefined) {
             luy = i;
             lux = j;
         } else {
             if (i < luy) luy = i;
             
             if (j < lux) lux = j;
         } 
            
         if (luy > rdy) rdy = luy;
         if (i > rdy) rdy = i;
         if (lux > rdx) rdx = lux;
         if (j > rdx) rdx = j;   
        }
    }

    answer.push(luy);
    answer.push(lux);
    answer.push(rdy+1);
    answer.push(rdx+1);
    
    return answer;
}