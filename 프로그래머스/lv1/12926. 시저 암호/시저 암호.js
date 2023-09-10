function solution(s, n) {
    var answer = '';
    let arr = s.split('');
    
    for(let el of arr) {
        let ascii = 0;
        if(el.charCodeAt() >= 65 && el.charCodeAt() <= 90) {
            ascii = el.charCodeAt() + n
            if(ascii > 90) ascii -= 26
            answer += String.fromCharCode(ascii);
        } else if(el.charCodeAt() >= 97 && el.charCodeAt() <= 122) {
            ascii = el.charCodeAt() + n
            if(ascii > 122) ascii -= 26
            answer += String.fromCharCode(ascii);
        } else answer += el
        
    }
    
    return answer;
}