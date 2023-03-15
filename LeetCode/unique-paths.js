/**
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
var uniquePathsDogshitSolution = function(m, n) {
    //let ar = [];
    let ar = new Array(m).fill(0).map(() => new Array(n).fill(0));

    let queue = [[0,0]]
    ar[0][0] = 1;
    while(queue[0] != undefined){
        const temp = queue.pop();

        let tempRight = [temp[0],temp[1]+1];
        let tempDown = [temp[0]+1,temp[1]];
        

        if(tempRight[1] <= n-1){
            queue.push(tempRight);
            ar[tempRight[0]][tempRight[1]]++;
        }

        if(tempDown[0] <= m-1){
            queue.push(tempDown);
            ar[tempDown[0]][tempDown[1]]++;
        }
    }
    return ar[m-1][n-1];
};


var uniquePaths = function(m, n) {
    //let ar = [];
    let ar = new Array(m).fill(0).map(() => new Array(n).fill(0));

    for(let i = 0;i<m;i++){
        ar[i][0] = 1; 
    }

    for(let j =0;j<n;j++){
        ar[0][j] = 1;
    }

    for(let i = 1;i < m;i ++){
        for(let j = 1;j<n;j++){
            ar[i][j] = ar[i-1][j] + ar[i][j-1];
        }
    }
    return ar[m-1][n-1];
};

console.log(uniquePaths(3,7))