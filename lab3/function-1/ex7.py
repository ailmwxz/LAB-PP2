def has_33(nums) :
    for i in range(len(nums)) :
            if nums[i] == 3 and nums[i + 1] == 3:
                 return False
            return True
my_list = list(input().split())
print(has_33(my_list))