function solution(todo_list, finished) {
    var answer = [];
    
    todo_list.forEach((todo,idx)=> {
        if(!finished[idx]) answer.push(todo)
    });
    
    return answer;
}