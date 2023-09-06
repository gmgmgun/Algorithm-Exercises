function solution(arr1, arr2) {
    
    var outer = [];
    var inner = [];
    
    for (let i = 0; i < arr1.length; i++) {
        inner = Array(arr1[i].length).fill(0);
        
        for (let j = 0; j < arr1[i].length; j++) {
            inner[j] = arr1[i][j] + arr2[i][j];
        }
        
        outer.push(inner);
    }
    
    return outer;
}