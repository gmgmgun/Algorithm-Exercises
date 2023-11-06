const solution = (num_list, n) => {
    let answer = [];
    let idx = 0;
    
    while(idx < num_list.length) {
        answer.push(num_list[idx]);
        idx += n;
    }
    
    return answer;
}