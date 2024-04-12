function solution(arr) {
    let idx = 0
    
    while(true) {
        const newArr = arr.map(a => {
            if(a >= 50 && a%2 === 0) return a/2
            if(a < 50 && a%2 === 1) return a*2+1
            return a
        })
       
        const isSame = arr.every((a, i) => a === newArr[i])
        
        if(isSame) break
        
        idx+=1

        arr = newArr
    }
    
    return idx
}