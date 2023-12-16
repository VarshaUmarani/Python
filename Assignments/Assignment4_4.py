# Write a program which contains filter(), map() and reduce() in it. Python application which contains one list of numbers. 
# List contains the numbers which are accepted from user.
# Filter should filter out all such numbers which are even.
# Map function will calculate its square.
# Reduce will return addition of all that numbers.

# Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
# List after filter = [2, 4, 4, 2, 8, 10]
# List after map = [4, 16, 16, 4, 64, 100] 
# Output of reduce = 204

import functools

def main():
	Arr = []

	Size = int(input("Enter Number of Elements : "))

	for i in range(Size):
		No = int(input("Enter Element Number {} : ".format(i+1)))
		Arr.append(No)

	print("Entered List is : ",Arr)

	FilteredData = list(filter((lambda No : (No % 2 == 0)),Arr))
	print("Filtered List is : ",FilteredData)

	MappedData = list(map((lambda No : No ** 2),FilteredData))
	print("Mapped List is : ",MappedData)

	Output = functools.reduce((lambda No1,No2 : No1 + No2),MappedData)
	print("Output of Reduce is : ",Output)

if __name__ == "__main__":
	main()