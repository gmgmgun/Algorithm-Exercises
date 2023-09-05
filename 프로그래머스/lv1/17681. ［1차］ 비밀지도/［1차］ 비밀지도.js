function solution(n, arr1, arr2) {
    let map = [];
    let answer = [];
    
    for(let i = 0; i < n; i++) {
        map.push((Number(arr1[i].toString(2)) + Number(arr2[i].toString(2))).toString().padStart(n,'0'));
        
        let str = '';    
        
        for (let j = 0; j < map[i].length; j++) {
            map[i][j] === '0' ? str += ' ' : str += '#' 
        }
        
        answer.push(str);
    }
    
    return answer;
}