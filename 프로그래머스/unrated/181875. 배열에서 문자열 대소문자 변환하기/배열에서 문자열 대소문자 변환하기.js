const solution = (arr) => {
    const answer = arr.map((str,idx) => idx%2 ? str.toUpperCase() : str.toLowerCase())
    
    return answer;
}