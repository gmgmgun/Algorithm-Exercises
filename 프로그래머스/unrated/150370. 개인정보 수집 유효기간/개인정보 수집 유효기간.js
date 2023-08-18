function convertedDate(str) {
   let amount = 0;
   const arr = str.slice(2).split('.')
   amount = (Number(arr[0])*12+Number(arr[1]))*28 + Number(arr[2])
   return amount;
}

function solution(today, terms, privacies) {
    const objTerm = {};
    const objPriv = {};
    const result =[];
    const convertedToday = convertedDate(today);
    
    for (let i = 0; i < terms.length; i++) {
        let val = '';
        for (let j = 2; j< terms[i].length; j++) {
               val += terms[i][j];
        }
        objTerm[terms[i][0]] = val;
    }
    
    for (let i = 0; i < privacies.length; i++) {
        const splited = privacies[i].split(' ');
        const validate = convertedDate(splited[0]) + Number(objTerm[splited[1]]) * 28;
        if (convertedToday >= validate) {
            result.push(i+1);
        }  
    }
    
    return result;
}