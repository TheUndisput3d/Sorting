from cyclic_sort import swap

def is_present(arr, num):
  for i in range(len(arr)):
    if arr[i] == num:
      return True
  return False

def missingNumber2(nums):
  n = len(nums)
  for i in range(n+1):
    is_present = False
    for j in range(len(nums)):
      if nums[j] == i:
        is_present = True
    if not is_present:
      return i

def missingNumber(nums):
  n = len(nums)
  for i in range(n+1):
    if not is_present(nums, i):
      return i

def missingNumber1(nums):
  n = len(nums)
  arr = set(nums)

  return list({i for i in range(n+1)} - arr)[0]

# cyclic sort approach for 0-n

def cyc_missing_num(nums):
  i = 0
  n = len(nums)
  while i < n:
    if nums[i] < n and nums[i] != nums[nums[i]]:
      swap(nums, i, nums[i])
    else:
      i += 1
  for i in range(n):
    if i != nums[i]:
      return i
  return n

def cyc_missing_num1(nums):
  i = 0
  n = len(nums)
  while i < n:
    correct = nums[i]
    if correct < n and nums[i] != nums[correct]:
      swap(nums, i, correct)
    else:
      i += 1
  for i in range(n):
    if i != nums[i]:
      return i
  return n

if __name__ == "__main__":
  nums = [9,6,4,2,3,5,7,0,1]
  print(f"func2: {missingNumber2(nums)}")
  print(f"func1: {missingNumber1(nums)}")
  print(f"func: {missingNumber(nums)}")
  print(f"cyc_sort: {cyc_missing_num(nums)}")

  
  