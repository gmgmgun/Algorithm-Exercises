function solution(absolutes, signs) {
    var answer = 0;
    for (idx in absolutes) signs[idx] ? answer += absolutes[idx] : answer -= absolutes[idx];
    return answer;
}