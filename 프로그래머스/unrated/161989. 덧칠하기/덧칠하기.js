function solution(n, m, section) {
    const wall = Array(n).fill(true);
    let index = 0;
    let cnt = 0;   

    for (let i=0; i<section.length; i++) {
        wall[section[i]-1] = false;
    }
    
    while(wall.indexOf(false) !== -1) {
        if(wall[index] === false) {
            cnt++;
            for(let i=index; i<index+m; i++) {
                wall[i]=true; 
            }
        }
        index++;
    }
    return cnt;
}