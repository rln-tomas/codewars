function addRemainders(nums, div){
    return nums.map(n => n + n % div)
}