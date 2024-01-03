# Accept N numbers from user and filter out only even numbers from that N numbers.
# After that add 2 in every even number.
# After the addition of 2 perform summation of that modified number.
# Using lambda function

# Size : 6
# Input : [1,3,2,4,6,5,4]
# After Filter : [2,4,6,4]
# After Map : [4,6,8,6]
# After Reduce : 24

# Using lambda Functions and passing the lambda function
# as a parameter directly to the in built functions. (filter,map,reduce)

from functools import reduce

def main():
	Arr = []

	Size = int(input("Enter Number of Elements : "))

	for i in range(Size):
		No = int(input("Enter Element {} : ".format(i+1)))
		Arr.append(No)

	print("Entered Data is : ",Arr)

	FilterData = list(filter((lambda No : (No % 2) == 0),Arr))
	print("Filtered Data is : ",FilterData)

	MappedData = list(map((lambda No : No + 2),FilterData))
	print("Mapped Data is : ",MappedData)

	ReducedData = reduce((lambda No1,No2 : No1 + No2),MappedData)
	print("Result is : ",ReducedData)

if __name__ == "__main__":
	main()