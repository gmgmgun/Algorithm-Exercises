function solution(arr, queries) {
    let temp = 0;
    
    for (let i = 0; i < queries.length; i++) {
        temp = arr[queries[i][0]];
        arr[queries[i][0]] = arr[queries[i][1]];
        arr[queries[i][1]] = temp;
    }
    
    return arr;
}