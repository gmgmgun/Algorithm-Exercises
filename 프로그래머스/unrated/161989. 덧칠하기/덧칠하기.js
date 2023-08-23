function solution(n, m, section) {
    const wall = Array(n).fill(true);
    let index = 0;
    let cnt = 0;   
    let falseCnt = 0;

    for (let i=0; i<section.length; i++) {
        wall[section[i]-1] = false;
        falseCnt++;
    }
    
    while(falseCnt > 0) {
        if(wall[index] === false) {
            cnt++;
            for(let i=index; i<index+m && i < n; i++) {
                if(!wall[i]){
                    wall[i]=true;
                    falseCnt--;
                }
            }
        }
        index++;
    }
    return cnt;
}