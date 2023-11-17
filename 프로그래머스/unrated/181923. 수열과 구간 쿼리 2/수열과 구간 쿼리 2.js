function solution(arr, queries) {
    var answer = [];
    
    queries.forEach((query)=> {
        const newArr = parseArr(arr,query[0],query[1]);
        const num = findNumber(newArr,query[2]);
        answer.push(num);
    })
    
    return answer;
}

function parseArr(arr,start,last) {
    return arr.slice(start,last+1)
}

function findNumber(arr,min) {
    let num = -1;
    
    arr.sort((a,b)=>b-a).forEach((el)=>{
        if(el>min) num = el;
    })
                        
    return num;
}