function solution(a, b) {

    let day = (a-1)*30 + b;

    while(1) {
        if(a === 1 || a === 3) break;
        
        if(a <= 5) {
            day+=1;
            break;
        }
        
        if(a <= 7) {
            day+=2;
            break;
        }
        
        if(a === 8) {
            day+=3;
            break;
        }
        
        if(a <= 10) {
            day+=4;
            break;
        }
        
        if(a <= 12) { 
            day+=5;
            break;
        }
    }
    
    switch (day%7) {
        case 0 : return "THU"
        break;
        case 1 : return "FRI"
        break;
        case 2 : return "SAT"
        break;
        case 3 : return "SUN"
        break;
        case 4 : return "MON"
        break;
        case 5 : return "TUE"
        break;
        case 6 : return "WED"
        break;
    }
}