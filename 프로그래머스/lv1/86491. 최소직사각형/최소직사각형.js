function solution(sizes) {
    var garo = [];
    var sero = [];
    
    for (let i = 0; i< sizes.length; i++) {
        garo.push(Math.max(...sizes[i]))
        sero.push(Math.min(...sizes[i]))
    }
    
    return Math.max(...garo) * Math.max(...sero)
}