# Accept N numbers from user and filter out only even numbers from that N numbers.
# After that add 2 in every even number.
# After the addition of 2 perform summation of that modified number.

# Size : 7
# Input : [1,3,2,4,6,5,4]
# After Filter : [2,4,6,4]
# After Map : [4,6,8,6]
# After Reduce : 24

# Using lambda functions

from functools import *

CheckEven = lambda No : (No % 2) == 0

Increment = lambda No : No + 2

Addition = lambda No1,No2 : No1 + No2

def main():
	Arr = []

	Size = int(input("Enter Number of Elements : "))

	for i in range(Size):
		No = int(input("Enter Element {} : ".format(i+1)))
		Arr.append(No)

	print("Entered Data is : ",Arr)

	FilteredData = list(filter(CheckEven,Arr))
	print("Filtered Data is : ",FilteredData)

	MappedData = list(map(Increment,FilteredData))
	print("Mapped Data is : ",MappedData)

	ReducedData = reduce(Addition,MappedData)
	print("Result is : ",ReducedData)

if __name__ == "__main__":
	main()