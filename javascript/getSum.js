function getSum(a, b){
    let initial, final, result = 0
    if (a === b) return a
    if (a < b){
        initial = a
        final = b
    }else{
        initial = b
        final = a
    }
    for (let i = initial; i <= final; i++){
        result = result + i
    }
    return result
}