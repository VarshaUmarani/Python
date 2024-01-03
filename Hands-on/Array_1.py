# Array n python
# Definition : Array is linear data structure which holds homogeneous elements in continous memory.
# and can be accessed in indexed format.

from array import *

def main():
	arr = array('i',[11,21,51,101,111])

	# <class 'array.array'>
	# array class from array module
	print("Type of arr is : ",type(arr))

	print("Length of array is : ",len(arr))

	print(arr)

	# Traversing array using for loop
	for i in range(len(arr)):
		print(arr[i],end="\t")
	print()

	# Traversing array using for each loop
	for no in arr:
		print(no,end="\t")
	print()

	# Traversing array using while loop
	iCnt = 0
	while iCnt != len(arr):
		print(arr[iCnt],end="\t")
		iCnt += 1
	print()

if __name__ == "__main__":
	main()