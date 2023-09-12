const solution = (nums) => {
    const arr = [...new Set(nums)];
    return nums.length/2 > arr.length ? arr.length : nums.length/2
}