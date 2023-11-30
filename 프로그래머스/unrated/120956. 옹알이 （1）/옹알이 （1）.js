function solution(babbling) {
    var answer = 0;
    
    babbling.forEach((bab)=>{
        if (foo(bab)) answer++;
    })
    
    return answer;
}

function foo(str) {
    const words = ['aya','ye','woo','ma'];
    
    words.forEach((word)=> {
        str = str.replace(word,'1');
    })
    
    const regex = new RegExp(`^[${1}]+$`);
    return regex.test(str);
}