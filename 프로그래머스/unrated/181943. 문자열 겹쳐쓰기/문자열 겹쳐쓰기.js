function solution(my_string, overwrite_string, s) {
    const my_arr = my_string.split('');
    let j = 0;
    
    for(let i = s; i < s + overwrite_string.length; i++) {
        my_arr[i] = overwrite_string[j];
        j++;
    }
    
    return my_arr.join('');
}