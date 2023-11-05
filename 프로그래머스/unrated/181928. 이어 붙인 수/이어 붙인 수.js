const solution = (num_list) => {
    let odd = '';
    let even = '';

    num_list.forEach((num) => num%2 ? odd+=num : even+=num);
    
    return Number(odd) + Number(even);
}