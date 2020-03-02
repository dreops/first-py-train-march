nums=[1,2,3,1]

def same_first_last(nums):
  if len(nums) >= 1:
    return True
  if nums[0] == nums[-1]:
    return True
  else:
    return False

print(len(nums))
print(nums[-1])

print (same_first_last(nums))