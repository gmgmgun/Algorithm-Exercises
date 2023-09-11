function solution(s) {
    let arr = s.split('');
    var answer = '';
    
    arr = arr.map(el=>el.charCodeAt()); 
    arr.sort((a,b)=>b-a);
    
    for(el of arr) answer += String.fromCharCode(el);
    
    return answer;
}