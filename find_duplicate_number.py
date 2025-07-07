from cyclic_sort import swap

def find_duplicate(nums):
  n = len(nums)
  i = 0
  while i < n:
    if nums[i] != nums[nums[i]-1]:
      swap(nums, i, nums[i]-1)
    else:
      i += 1
  for i in range(len(nums)):
    if nums[i] != i+1:
      return nums[i]



if __name__ == "__main__":  
  nums = [1, 3, 4, 5, 5]
  print(find_duplicate(nums))
