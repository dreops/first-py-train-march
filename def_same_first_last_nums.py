
nums = [1,2,3,4]

def same_first_last(nums):
    if len(nums) >= 1 and nums[0] == nums[-1]:
        return True
    else:
        return False

print (same_first_last(nums))