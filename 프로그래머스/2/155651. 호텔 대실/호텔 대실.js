function solution(book_time) {
    const rooms = [];
    
    const newTime = book_time.map(([s,e])=>{
        const [sh,sm] = s.split(':').map(str=>Number(str));
        const [eh,em] = e.split(':').map(str=>Number(str));

        return [sh * 60 + sm , eh * 60 + em + 10];
    })

    newTime.sort((a,b)=>a[0] - b[0]);
    newTime.forEach(([st,et])=>{
        if(Math.min(...rooms) > st){
            rooms.push(et);
        }
        else{
            const minIdx = rooms.indexOf(Math.min(...rooms));
            rooms.splice(minIdx,1,et);
        }
    })

    return rooms.length;
}