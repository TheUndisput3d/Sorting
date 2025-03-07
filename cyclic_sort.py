def cyclic_sort1(arr):
  for i in range(len(arr)-1):
    while i != arr[i] -1:
      swap(arr, i, arr[i]-1)

def cyclic_sort(arr): ## best approach
  i = 0
  while i < len(arr):
    correct = arr[i] - 1
    if arr[i] != arr[correct]:
      swap(arr, i, correct)
    else:
      i += 1

def swap(arr, first, sec):
  temp = arr[first]
  arr[first] = arr[sec]
  arr[sec] = temp

if __name__ == "__main__":
  arr = [3, 2, 1]
  cyclic_sort(arr)
  # cyclic_sort1(arr)
  print(arr)

