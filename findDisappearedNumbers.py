from cyclic_sort import swap

def findDisappearedNumbers(nums):
  n = len(nums)
  i = 0
  res = []
  while i < len(nums):
    if nums[i] != nums[nums[i] - 1]:
      swap(nums, i, nums[i]-1)
    else:
      i += 1
  print(nums)
  
  for i in range(len(nums)):
    if nums[i] != i+1:
      res.append(i+1)
  return res

print(findDisappearedNumbers([1, 1, 1, 1]))

  
