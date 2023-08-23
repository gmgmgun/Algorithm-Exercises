function solution(s) {
    var answer = 0;
    var word = s[0];
    var cnt1 = 0;
    var cnt2 = 0;
    
    for (let i = 0; i < s.length; i++) {
        s[i] === word ? cnt1++ : cnt2++
        if (cnt1 === cnt2) {
            word = s[i+1];
            answer++;
        } else if (i === s.length-1) {
            answer++;
        }
    }
    return answer;
}