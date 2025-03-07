def insertion_sort(arr):
  for i in range(len(arr)-1):
    for j in range(i+1, 0, -1):  
      if arr[j] < arr[j-1]:
        swap(arr, j, j-1)
      else:
        break

def swap(arr, ind1, ind2):
  temp = arr[ind1]
  arr[ind1] = arr[ind2]
  arr[ind2] = temp

if __name__ == "__main__":
  arr = [5, 4, 3, 2, 1]
  print(f"before_sorting:", arr)
  insertion_sort(arr)
  print(arr)
