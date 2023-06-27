function checkCard(cards1, cards2, card) {
    
    if (cards1.indexOf(card) !== -1){
        return 1;
    } else if (cards2.indexOf(card) !== -1) {
        return 2;
    } else {
        return -1;
    }
    
}

function solution(cards1, cards2, goal) {
    var answer = "Yes";
    
    const check1 = Array(cards1.length).fill(false);
    const check2 = Array(cards2.length).fill(false);

    for (let i =0; i< goal.length; i++) {
        var cardsNum = checkCard(cards1, cards2, goal[i]);
        var index = 0;  
        
        if (cardsNum === 1) {
            index = cards1.indexOf(goal[i]);
        } else {
            index = cards2.indexOf(goal[i]);
        }
        
        if (cardsNum === 1) {
            for (let j =0; j< index; j++) {
              if (check1[j] === false) {
                  answer = "No"
              }  
            }
            check1[index] = true;
        } else {
            for (let j =0; j< index; j++) {
              if (check2[j] === false) {
                  answer = "No"
              }  
            }
            check2[index] = true;
        }
    }
    
    return answer;
}
