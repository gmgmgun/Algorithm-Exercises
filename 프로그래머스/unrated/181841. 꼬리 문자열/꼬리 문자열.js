function solution(str_list, ex) {
    var answer = '';
    
    str_list.forEach(str=> {
        if(str.indexOf(ex) === -1) {
            answer += str;
        }
    })
    
    return answer;
}