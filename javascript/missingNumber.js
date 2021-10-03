function missingNo(nums){
    let i; 
    for ( i=1; i < 101; i++){
        if (!nums.includes(i)) return i
    }
}