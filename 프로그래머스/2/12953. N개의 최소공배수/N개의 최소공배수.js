function solution(arr) {
    const getGCD = (a,b) => {
        if (a%b===0) return b
        return getGCD(b,a%b)
    }
    
    const getLCM = (a,b) => a*b/getGCD(a,b)
   
    return arr.reduce((a,c) => getLCM(a,c),1)
}