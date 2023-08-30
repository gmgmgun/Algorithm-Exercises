function solution(numbers) {
    return 45 - numbers.reduce((acc,el) => acc+el)
}