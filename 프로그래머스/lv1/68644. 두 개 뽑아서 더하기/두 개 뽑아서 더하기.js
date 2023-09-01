function solution(numbers) {
    var answer = [];
    for (let i = 0; i < numbers.length; i++) {
        for (let j = 0; j < numbers.length; j++) {
            if (i !== j && answer.indexOf(numbers[i] + numbers[j]) === -1) {
                answer.push(numbers[i] + numbers[j])
            }
        }    
    }
    
    return answer.sort((a,b) => a-b);
}