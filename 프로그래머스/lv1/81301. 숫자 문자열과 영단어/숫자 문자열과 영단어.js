function solution(s) {
    const obj = {
        '0' : 'zero',
        '1' : 'one',
        '2' : 'two',
        '3' : 'three',
        '4' : 'four',
        '5' : 'five',
        '6' : 'six',
        '7' : 'seven',
        '8' : 'eight',
        '9' : 'nine',
    }
    
    for (el in obj) {
        var idx = 0;
        
        while (idx !== -1) {
            idx = s.indexOf(obj[el]);
            if(idx !== -1) {
                s = s.substring(0, idx) + el + s.substring(idx + obj[el].length);
            }
        } 
    }
    
    return Number(s);
}