function getDivisorsCount(num){
    return [...Array(num+1).keys()].filter(x => num % x === 0).length
}