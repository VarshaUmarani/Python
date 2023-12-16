# Accept N numbers  from user and filter - out only even numbers from those N numbers.
# After that Add 2 in every even number.
# After the Addition by 2 then perform Summation of those modified number.

# Size : 7
# Input        : [1,3,2,4,6,5,4]
# After Filter : [2,4,6,4]
# After Map    : [4,6,8,6]
# After Reduce : 24

# Using lambda Functions and passing the lambda function
# as a parameter directly to the in built functions. (filter,map,reduce) 

from functools import reduce

def main():
	Arr = []
	print("Enter the Number of Elements : ")
	Size = int(input())

	for i in range(Size):
		Value = int(input("Enter Element at {} : ".format(i+1)))
		Arr.append(Value)

	print("Entered Data is :",Arr)

	Output = reduce(lambda No1,No2 : No1 + No2,list(filter(lambda No : (No % 2 == 0),list(map(lambda No : No + 2,Arr)))))
	print("Final Result is :",Output)

if __name__ == "__main__":
	main()

# 	FilteredData = list(filter(lambda No : (No % 2 == 0),Arr))
#	print("After Filtering Data is :",FilteredData)

#	MappedData = list(map(lambda No : No + 2,NewData))
#	print("After Mapping Data is :",MappedData)