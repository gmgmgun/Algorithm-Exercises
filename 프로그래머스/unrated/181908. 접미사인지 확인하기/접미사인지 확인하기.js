function solution(my_string, is_suffix) {
    const length = is_suffix.length;
    const index = my_string.lastIndexOf(is_suffix);
    
    if(index === -1) return 0;
    
    if(index+length === my_string.length) return 1;
    
    return 0;
}