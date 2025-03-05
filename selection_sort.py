def selection_sort(arr):
  n = len(arr)
  for i in range(n-1):
    last = n-i-1

    max_index = get_max_index(last, arr)
    if arr[last] != arr[max_index]:
      arr[last], arr[max_index] = arr[max_index], arr[last]

def get_max_index(last, array):
  max_ = 0
  for i in range(1, last+1):
    if array[i] > array[max_]:
      max_ = i
  return max_

def rec_selection_sort(arr, last_index, n): # simple recursive selection sort
  if n == 1:
    return 
  max_index = get_max_index(last_index, arr)
  if arr[last_index] != arr[max_index]:
    arr[last_index], arr[max_index] = arr[max_index], arr[last_index]
  rec_selection_sort(arr, last_index-1, n-1)

  

if __name__ == "__main__":
  arr = [7, 6, 5, 4, 3, 2, 1]
  print("before sorting:",arr)
  rec_selection_sort(arr, len(arr)-1, len(arr))
  print("after sorting:", arr)


  