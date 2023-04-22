const numSortLambda = (a,b) =>{
    return a-b;
}
var merge = function(intervals) {
    const map = new Map();
    intervals.forEach((item) =>{
        //console.log(item);
        if(!map.has(item[0])){
            map.set(item[0],item);
        }else{
            var it = map.get(item[0])
            if(it[1] < item[1]){
                it[1] = item[1];
            }
        }
    });

    //console.log(map)
    
    //console.log([...map.keys()])
    var ar = [...map.keys()]

    let retIntervals = [];
    let prevMax = -1;
    ar.sort(numSortLambda).forEach((itemKey) => {
        let item = map.get(itemKey);
        //console.log(`${itemKey} and ${item}`)
        if(item[0] > prevMax){
            retIntervals.push(item);
            prevMax = item[1];
        }else{
            if(item[1] > prevMax){
              let temp = retIntervals.pop();   
              temp[1] = item[1];
              retIntervals.push(temp);
              prevMax = item[1]
            }
        }
    })
    return retIntervals;
    //console.log(retIntervals)
};


console.log(merge([]))
