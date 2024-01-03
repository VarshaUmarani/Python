# Accept N numbers from user and filter out only even numbers from that N numbers.
# After that add 2 in every even number.
# After the addition of 2 perform summation of that modified number.

# Size : 7
# Input : [1,3,2,4,6,5,4]
# After Filter : [2,4,6,4]
# After Map : [4,6,8,6]
# After Reduce : 24

# Using User Defining Functions

def CheckEven(No):
	if No % 2 == 0:
		return True
	else:
		return False

# Filter
def Filter(List):
	Arr = []
	for i in range(len(List)):
		if CheckEven(List[i]) == True:
			Arr.append(List[i])

	return Arr

# Map
def Map(List):
	for i in range(len(List)):
		List[i] = List[i] + 2

	return List

# Reduce
def Reduce(List):
	Sum = 0
	for i in range(len(List)):
		Sum = Sum + List[i]

	return Sum

def main():
	Arr = []

	Size = int(input("Enter Number of Elements : "))

	for i in range(Size):
		No = int(input("Enter Element Number {} : ".format(i+1)))
		Arr.append(No)

	print("Entered Data is : ",Arr)

	FilteredData = Filter(Arr)
	print("Filtered Data is : ",FilteredData)

	MappedData = Map(FilteredData)
	print("Mapped Data is : ",MappedData)

	ReducedData = Reduce(MappedData)
	print("Reduced Data is : ",ReducedData)

if __name__ == "__main__":
	main()