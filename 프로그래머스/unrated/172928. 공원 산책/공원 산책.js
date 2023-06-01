function solution(park, routes) {
    const sero = park.length-1;
    const garo = park[0].length-1;
    const current = [];
    let cnt = 0;
    for(let i = 0; i< park.length; i++) {
        for(let j = 0; j<park[0].length; j++){
            if (park[i][j] === "S") {
                current.push(i);
                current.push(j); 
            }
        }
    }
    
    for(let i=0; i< routes.length; i++) {
        let cnt = 0;
        switch (routes[i][0]) {
          case "E" :
                if (current[1] + Number(routes[i][2]) > garo) break;
                
                for(let j = 1; j <= Number(routes[i][2]); j++ ) {
                    if(park[current[0]][current[1]+j] === "X") cnt++;
                }               
                
                if(cnt ===0) current[1] = current[1] + Number(routes[i][2]);
         break;
         case "W" :
                if (current[1] - Number(routes[i][2]) < 0) break;
            
                for(let j = 1; j <= Number(routes[i][2]); j++ ) {
                    if(park[current[0]][current[1]-j] === "X") cnt++;
                }              
            
                if (cnt === 0) current[1] = current[1] - Number(routes[i][2]);                  
         break;
          case "S" :
                if (current[0] + Number(routes[i][2]) > sero) break;

                for(let j = 1; j <= Number(routes[i][2]); j++ ) {
                    if(park[current[0]+j][current[1]] === "X") cnt++;
                }
                
                if(cnt === 0) current[0] = current[0] + Number(routes[i][2]);    
                
         break;
         case "N" :    
                if (current[0] - Number(routes[i][2]) < 0) break;
                
                for(let j = 1; j <= Number(routes[i][2]); j++ ) {
                   if(park[current[0]-j][current[1]] === "X") cnt++;
                }
                
                if(cnt === 0) current[0] = current[0] - Number(routes[i][2]);    
         break;
         default :
        }
    }
        
    return current;
}