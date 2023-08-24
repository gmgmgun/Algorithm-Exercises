function solution(food) {
    var answer = '';
    let arr = [0];
    
    for (let i = food.length-1; i >= 1 ; i--) {
        for(let j = 0; j < parseInt(food[i]/2); j++) {
            arr.push(i);
            arr.unshift(i);
        }
    }
    
    answer = arr.join('');
    
    return answer;
}