# Linear Search
def find(arr, x):
   for i in range(len(arr)):	
     if arr[i] == x:
       return i 
   return -1

# Binary Search 
def binary_search(arr, x): 
  left = 0
  right = len(arr)-1

  mid = (left + right) // 2
  while left<=right and arr[mid] != x: 

      print("index mid:", arr[mid])
      if arr[mid] > x: # x must be located in the first half
        right = mid - 1

      elif arr[mid] < x: # x must be located in second half 
        left = mid + 1

      mid = (left + right) // 2

  print("index", mid,":", arr[mid])
  if left <= right: 
    return mid
  else: 
    -1   

def hello_course():
  return("Hello 2132!")

def hello_world():
  return "Hello World!"

if __name__ == "__main__":

  li = [1, 7, 13, 23, 42, 55, 100]
  x = 55 
  # calling binary search
  index = binary_search(li, x)
  print("Found",x,"at index",index)

  # calling linear search for comparison

  index = find(li, x)
  print("Found",x,"at index",index)

