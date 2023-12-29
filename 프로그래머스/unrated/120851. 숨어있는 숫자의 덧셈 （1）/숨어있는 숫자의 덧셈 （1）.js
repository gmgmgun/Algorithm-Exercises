function solution(my_string) {
    var answer = 0;
   
    [...my_string].forEach(str=> {
        if(Number(str)) answer += Number(str);
    })

    return answer;
}