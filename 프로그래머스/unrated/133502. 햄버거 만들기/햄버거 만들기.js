function solution(ingredient) {
    let answer = 0;
    let flag = true;
    let i = 0;
    
    while (flag) {
        if (ingredient[i] === 1 && ingredient[i+1] === 2 && ingredient[i+2] === 3 && ingredient[i+3] === 1) {
            ingredient.splice(i,4);
            i = i - 3;
            answer++;
        } else if (i > ingredient.length - 3) {
            flag = false;
        } else {
            i++;
        }
    }
    
    return answer;
}