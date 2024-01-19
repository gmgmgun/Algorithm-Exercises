function solution(my_string) {
    let answer = '';
    
    my_string.split('').forEach(el => {
        if(el === el.toUpperCase()) {
            answer += el.toLowerCase();        
        } else {
            answer += el.toUpperCase();
        }
    })
    
    return answer;
}