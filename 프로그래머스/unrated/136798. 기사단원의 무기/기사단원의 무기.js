function solution(number, limit, power) {
    let answer = 0;
    let yaksuArr = Array(number).fill(1);

    for (let i = 2; i <= number; i++) {
        for (let j = i; j <= number; j += i) {
            yaksuArr[j-1]++;
        }
    }

    answer = yaksuArr.map(el => el > limit ? power : el).reduce((acc, val) => acc + val);

    return answer;
}