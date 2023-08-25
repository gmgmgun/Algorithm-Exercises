function solution(babbling) {
    var answer = 0;
    var words = [ "aya", "ye", "woo", "ma"];
    
    for (let i = 0; i < babbling.length; i++) {
        let str = babbling[i];
        let dupCheck = true;
        
        for (let j = 0; j < words.length; j++) {
            str = str.replaceAll(words[j],j+1);
        }
        
        for (let k = 0; k < str.length; k++) {
            if(Number(str[k])) {
                if(str[k] === str[k+1]) {
                    dupCheck = false;
                }
            }
        }
        
        if(Number(str) >= 0 && dupCheck) answer++;
    }
    
    return answer;
}