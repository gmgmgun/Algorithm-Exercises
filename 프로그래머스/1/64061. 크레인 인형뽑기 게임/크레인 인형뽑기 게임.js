function solution(board, moves) {
    var answer = 0;
    let cols = [];
    let buck = [];
    
    for (let i = 0; i< board.length; i++) {
        let col = [];
        for (let j = 0; j< board[i].length; j++) {
            if(board[j][i]) col.push(board[j][i])
        }
        cols.push(col);
        console.log(cols)
    }
        
    for (el of moves) {
        if(cols[el-1].length) {
            if (cols[el-1][0] === buck[buck.length-1]) {
                buck.pop();
                cols[el-1].shift();
                answer += 2;
            } else {
                buck.push(cols[el-1].shift()); 
            }
        }
    }
    
    return answer;
}
