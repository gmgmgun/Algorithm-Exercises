function solution(s1, s2) {
    var answer = 0;
    s1.forEach(el=> {
        if (s2.indexOf(el) !== -1) answer++;
    })
    return answer;
}