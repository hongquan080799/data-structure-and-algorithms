arr = [1,2,4,5,6,7,8,9]
def remove(array, value):
  found = False
  for i in range(len(array)):
    if array[i] == value:
      for j in range(i + 1, len(array)):
        array[j - 1] = array[j]
      array.pop()
      found = True
      break

  if not found:
    raise ValueError(f"Value {value} not found in the array")

def insert(array, value, index):
    if index < 0 or index > len(array):
        raise IndexError("Index out of bounds")
    for i in range(len(array) - 1, index - 1, -1):
        array[i] = array[i - 1]
    array[index] = value

my_array = [1, 2, 4, 5, None]
insert(my_array, 3, 2)

# # Example usage
# my_array = [1, 2, 3, 4, 2]
# remove(my_array, 3)

print(my_array)  
