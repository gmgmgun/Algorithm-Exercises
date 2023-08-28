function solution(X, Y) {
    var answer = '';
    let freqMap = {};

    for (let num of Y) {
        if (freqMap[num]) {
            freqMap[num]++;
        } else {
            freqMap[num] = 1;
        }
    }

    for (let num of X) {
        if (freqMap[num] && freqMap[num] > 0) {
            answer += num;
            freqMap[num]--;
        }
    }

    if (!answer) return "-1";
    else if (answer[0] === "0") return "0";

    return answer.split('').sort((a, b) => b - a).join('');
}
