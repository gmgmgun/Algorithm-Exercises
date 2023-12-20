function solution(s) {
    let count = 0;
    let totalDiff = 0;
    let str = s;
    
    while(str !== "1") {
        [str, diff] = foo(str);
        count++;
        totalDiff += Number(diff);
        str = str.length.toString(2);
    }
    
    return [count,totalDiff];
}

function foo(string) {
    const str = string.split('').filter(el=> el !== '0').join('');
    const diff = string.length - str.length;
    return [str,diff];
}