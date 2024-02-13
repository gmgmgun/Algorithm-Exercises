function solution(myString, pat) {
    const changedStr = myString.split('').map(el => el === "A" ? "B" : "A").join('');
    return changedStr.indexOf(pat) === -1 ? 0 : 1
}