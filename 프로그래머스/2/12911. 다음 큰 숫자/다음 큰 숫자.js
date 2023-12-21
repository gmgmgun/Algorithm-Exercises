function solution(n) {
    const countOnes = (num) => num.toString(2).split('0').join('').length;

    const targetCount = countOnes(n);
    
    let answer = n + 1;

    while (countOnes(answer) !== targetCount) {
        answer++;
    }

    return answer;
}