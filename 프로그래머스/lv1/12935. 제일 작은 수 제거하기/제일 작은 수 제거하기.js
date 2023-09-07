function solution(arr) {
    let minIdx = 0;
    let min = arr[0];
    
    for(idx in arr) {
        if (arr[idx] < min) {
            min = arr[idx];
            minIdx = idx;
        }
    }
    
    arr = arr.filter((el,idx)=>idx!=minIdx)
    
    if(arr.length) return arr;
    else return [-1];
}