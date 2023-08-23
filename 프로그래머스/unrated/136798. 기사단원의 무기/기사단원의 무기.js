function solution(number, limit, power) {
    let answer = 0;
    let yaksuArr = Array(number + 1).fill(1);

    for (let i = 2; i <= number; i++) {
        for (let j = i; j <= number; j += i) {
            yaksuArr[j]++;
        }
    }

    answer = yaksuArr.slice(1).map(el => el > limit ? power : el).reduce((acc, val) => acc + val);

    return answer;
}