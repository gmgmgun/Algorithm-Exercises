const solution = (str) => {
    const arr = str.split('');
    const answer = arr.map((word)=> {
        if(word === 'm') return 'rn';
        return word;
    });
    
    return answer.join('');
}