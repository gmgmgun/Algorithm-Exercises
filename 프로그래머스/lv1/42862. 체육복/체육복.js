function solution(n, lost, reserve) {
    var answer = n-lost.length;
    
    reserve = reserve.sort((a,b)=>a-b)
    lost = lost.sort((a,b)=>a-b)

    // 중복 먼저 제거
    for (el of lost) {
        if (reserve.indexOf(el) !== -1) {
            reserve = reserve.filter((_,idx) => idx !== reserve.indexOf(el))
            lost = lost.filter((_,idx) => idx !== lost.indexOf(el))
            answer++;
        }
    }
    
    //나머지 연산
    for (el of lost) {
        if (reserve.indexOf(el-1) !== -1) {
            reserve = reserve.filter((_,idx) => idx !== reserve.indexOf(el-1))
            lost = lost.filter((_,idx) => idx !== lost.indexOf(el))
            answer++;
        } else if (reserve.indexOf(el+1) !== -1) {
            reserve = reserve.filter((_,idx) => idx !== reserve.indexOf(el+1))
            lost = lost.filter((_,idx) => idx !== lost.indexOf(el))
            answer++;
        }   
    }
    
    return answer;
}