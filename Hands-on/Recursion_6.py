# Accept N numbers from user and find addition of all that N numbers.
# Using for loop
# Using while loop
# Using Recursive method

# Size : 7
# Input : [1,3,2,4,6,5,4]
# Output : 25

Add = 0
i = 0

def AdditionFor(List):
	Sum = 0
	for i in range(len(List)):
		Sum = Sum + List[i]

	return Sum

def AdditionWhile(List):
	Sum = 0
	i = 0

	while i != len(List):
		Sum = Sum + List[i]
		i = i + 1

	return Sum

def AdditionRecursive(List):
	global Add, i

	if i != len(List):
		Add = Add + List[i]
		i = i + 1
		AdditionRecursive(List)

	return Add

def main():
	Arr = []

	Size = int(input("Enter Number of Elements : "))

	for i in range(Size):
		Arr.append(int(input("Enter Element {} : ".format(i+1))))

	print("Entered Elements are : ",Arr)

	Ret = AdditionFor(Arr)
	print("Addition of Elements using for loop is : ",Ret)

	Ret = AdditionWhile(Arr)
	print("Addition of Elements using while loop is : ",Ret)

	Ret = AdditionRecursive(Arr)
	print("Addition of Elements using recursive function is : ",Ret)

if __name__ == "__main__":
	main()