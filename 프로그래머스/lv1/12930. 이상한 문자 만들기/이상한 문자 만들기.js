function solution(s) {
    var answer = '';
    let idx = 0;
    let cnt = 0;
    
    while(idx<s.length) {
        if(s[idx] !== ' ') {
            if(cnt%2) answer += s[idx].toLowerCase();
            else answer += s[idx].toUpperCase();
            cnt++;
        } else {
            answer += s[idx];
            cnt = 0;
        }
        idx++;
    }
    
    return answer;
}