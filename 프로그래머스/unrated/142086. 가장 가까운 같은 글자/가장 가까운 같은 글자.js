function solution(s) {
    var answer = [];
    var obj = {};

    for (let i = 0; i < s.length; i++) {
        obj[s[i]] === undefined ? answer.push(-1) : answer.push(i-obj[s[i]]);
        obj[s[i]] = i;
    }

    return answer;
}