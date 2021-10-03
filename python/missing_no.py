def missing_no(nums): 
    for i in range(0, 101): 
        try:
            nums.index(i)
        except ValueError: 
            return i
    