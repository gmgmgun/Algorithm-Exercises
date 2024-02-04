function solution(arr, delete_list) {
    const answer = [];
    
    arr.forEach(el => {
        if(delete_list.indexOf(el) === -1) answer.push(el);
    });
    
    return answer;
}