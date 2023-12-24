function solution(n, words) {
    //words에서 n개까지 담아
    //indexOf해서 인덱스 찾은 다음에 n으로 나눠서 몫과 나머지 리턴 !
    const stack = [];
    
    for(let i = 0; i < words.length; i++) {
        if (words[i-1] && (words[i-1][words[i-1].length-1] !== words[i][0])) {
            return [(i+1)%n ? (i+1)%n : n ,Math.ceil((i+1)/n)];
        }
        else if (stack.indexOf(words[i]) !== -1) return [(i+1)%n ? (i+1)%n : n,Math.ceil((i+1)/n)];
        
        stack.push(words[i]);
    }
    
    return [0,0];
}