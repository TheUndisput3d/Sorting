arr = [5, 4, 3, 2, 1]

# bubble sort takes a total of n-1 passes where,  n= len(arr)

def bubble_sort(arr):
  is_swapped = False
  for i in range(len(arr)-1):
    for j in range(1, len(arr)-i):
      if arr[j] < arr[j-1]:
        arr[j], arr[j-1] = arr[j-1], arr[j]
        is_swapped = True
  
    if not is_swapped:
      break

def rec_bubble(arr, n, c):
  if c == len(arr) -1:
    return
  for i in range(1, n):
    if arr[i] < arr[i-1]:
      arr[i], arr[i-1] = arr[i-1], arr[i]
  rec_bubble(arr, n-1, c+1)


if __name__ == "__main__":
  print(f"unsorted_array: {arr}")
  rec_bubble(arr, 5, 0)
  print(f"sorted_array: {arr}")
