function solution(dot) {
    if(foo(dot)) {
        if(dot[0] > 0) return 1;
        return 3;
    } 
    
    if(dot[0] > 0) return 4;
    return 2;
}

const foo = (dot) => dot[0] * dot[1] >= 0;