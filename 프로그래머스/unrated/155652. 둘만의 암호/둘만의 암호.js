function charToAscii(str) {
    const arr = Array.from(str);
    
    const asciiArr = arr.reduce(function(result, element) {
        element = element.charCodeAt(0) - 97;
        result.push(element);
        return result;
    }, []);
    
    return asciiArr;
}

function solution(s, skip, index) {
    var answer = '';
    
    const sArr = charToAscii(s);
    const skipArr = [...new Set(charToAscii(skip))];
    for (let i = 0; i < sArr.length; i++) {
        let jump = 0;
        let newChar = sArr[i] + index;
        let flag = 0;
       
        if (newChar > 25) {
            newChar -= 26;
            flag = 1;
        }
       
        
        for(let j = 0; j < skipArr.length; j++) {
            if (flag === 0) {
                if(skipArr[j] > sArr[i] && skipArr[j] <= newChar) {
                    jump ++;
                }    
            } else {
                if(skipArr[j] > sArr[i] || skipArr[j] <= newChar) {
                    jump ++;
                }
            }
        }
        
        newChar += jump;
        
        if(newChar > 25) {
            newChar -= 26;
        }
        
        const char = String.fromCharCode(newChar+97);
        
        answer += char;
    }
    
    return answer;
}