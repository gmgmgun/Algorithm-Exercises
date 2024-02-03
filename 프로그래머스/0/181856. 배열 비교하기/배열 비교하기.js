const solution = (arr1,arr2) => {
    if(arr1.length > arr2.length) return 1;
    if(arr1.length < arr2.length) return -1;
    if(arr1.reduce((acc,cur) => acc+cur,0) > arr2.reduce((acc,cur) => acc+cur,0)) return 1;
    if(arr1.reduce((acc,cur) => acc+cur,0) < arr2.reduce((acc,cur) => acc+cur,0)) return -1;
    return 0;
}