def add_remainders(nums, div): 
    return [num  + (num % div) for num in nums ]
