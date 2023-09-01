const getRowCol = (num) => {
    const pad = [[1,2,3],[4,5,6],[7,8,9],['*',0,'#']];
    let row = 0;
    
    for (r of pad) {
        if (r.indexOf(num) !== -1) return [row,r.indexOf(num)];   
        row++;
    }
}

function solution(numbers, hand) {
    var answer = '';
    let left = [3,0];
    let right = [3,2];
    
    for (num of numbers) {
        const next = getRowCol(num);
        if (next[1] === 0) {
            answer += 'L';
            left = next;
        }
        else if (next[1] === 2) {
            answer += 'R';
            right = next;
        }
        else {
            if (Math.abs(next[0] - left[0]) + Math.abs(next[1] - left[1]) < Math.abs(next[0] - right[0]) + Math.abs(next[1] - right[1])) {
                answer += 'L';
                left = next;
            } else if (Math.abs(next[0] - left[0]) + Math.abs(next[1] - left[1]) > Math.abs(next[0] - right[0]) + Math.abs(next[1] - right[1])) {
                answer += 'R';
                right = next;
            }
            else {
                if (hand === 'left') {
                    answer += 'L';
                    left = next;
                } else {
                    answer += 'R';
                    right = next;
                }
            }
        }
    }
    return answer;
}