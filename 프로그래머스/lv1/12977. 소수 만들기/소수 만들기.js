function solution(nums) {
    nums.sort((a,b)=>a-b);
    
    let cnt = 0;
    
    for (let i = 0; i < nums.length-2; i++) {
        for (let j = i+1; j < nums.length-1; j++) {
            for (let k = j+1; k < nums.length; k++) {
                if(isPrime(nums[i]+nums[j]+nums[k])) cnt++;
            }   
        }
    }
    
    return cnt;
}

const isPrime = (num) => {
    for (let i = 2; i<num/2; i++) {
        if (num%i === 0) return false;
    }
    return true;
}