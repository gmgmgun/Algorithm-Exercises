function solution(my_string, index_list) {
    return index_list.reduce((acc,idx)=> acc += my_string[idx],'');
}