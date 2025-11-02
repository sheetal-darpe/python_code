from numpy import *

# arr = array([1,2,3,4])

# print(arr.dtype)

# arr = int(array([1,2.0,3,4]))
# print(arr.dtype)


arr = []
for x in range(3):
    num = input("Enter a number: ")
    arr.append(num)

print("Numbers entered:", arr)