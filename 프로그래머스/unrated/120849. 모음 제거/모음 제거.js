const solution = (my_string) => {
    const vowels = ['a','e','i','o','u'];
    const arr = [];
    
    my_string.split('').forEach(el => {
        if(vowels.indexOf(el) === -1) arr.push(el); 
    })

    return arr.join('');
}