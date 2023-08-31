function solution(new_id) {
    var answer = '';
    //아이디의 길이는 3자 이상 15자 이하여야 합니다.
    //아이디는 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.) 문자만 사용할 수 있습니다.
    //단, 마침표(.)는 처음과 끝에 사용할 수 없으며 또한 연속으로 사용할 수 없습니다.
    //48-57 //97-122
    
    new_id = new_id.toLowerCase();
    
    for (el of new_id) {
        if((el.charCodeAt() >= 48 && el.charCodeAt() <= 57) || (el.charCodeAt() >= 97 && el.charCodeAt() <= 122) || el === '-' || el === '_' || el === '.') {
        }
        else {
            new_id = new_id.replace(el,'');
        }
    }

    while(new_id.indexOf('..') !== -1) {
        new_id = new_id.replaceAll('..','.')
    }
    
    if (new_id[0] === '.') new_id = new_id.slice(1,new_id.length);
    
    if (new_id[new_id.length-1] === '.') new_id = new_id.slice(0,new_id.length-1);
    
    if (new_id === '') new_id = 'a';
    
    if (new_id.length >= 16) {
        new_id = new_id.slice(0,15);
        if (new_id[new_id.length-1] === '.') new_id = new_id.slice(0,new_id.length-1);
    }
    
    if (new_id.length <= 2) {
        while(new_id.length < 3) {
            new_id += new_id[new_id.length-1];
        }
    }
    
    return new_id;
}