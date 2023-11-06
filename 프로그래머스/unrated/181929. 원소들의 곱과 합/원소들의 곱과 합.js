const solution = (num_list) => {
    const multi = num_list.reduce((acc,cur)=>acc*cur);
    const sum = num_list.reduce((acc,cur)=>acc+cur);
    
    return sum*sum > multi ? 1 : 0;  
}