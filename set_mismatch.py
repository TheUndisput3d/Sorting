def set_mismatch(nums): ## best approach
  i = 0
  while i < len(nums):
    if nums[i] != nums[nums[i] - 1]:
      swap(nums, i, nums[i] - 1)
    else:
      i += 1

def swap(arr, first, sec):
  temp = arr[first]
  arr[first] = arr[sec]
  arr[sec] = temp