function solution(array) {
    let num = 0;
    let numIdx = 0;
    
    array.forEach((el,idx) => {
        if(el > num) {
            num = el;
            numIdx = idx;
        }
    })
                  
    return [num,numIdx];
}