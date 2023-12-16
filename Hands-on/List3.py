# Accept N numbers from user and return addition of those N numbers.

# Size : 5
# Input : [5,4,3,1,2]
# Output : 5 + 4 + 3 + 2 + 1 = 15

def Summation(List):
	Sum = 0
	for i in range(len(List)):
		Sum = Sum + List[i]
	return Sum

def main():
	Arr = []

	Size = int(input("Enter Number of Elements : "))

	for i in range(Size):
		No = int(input("Enter Element No {} : ".format(i+1)))
		Arr.append(No)

	Ret = Summation(Arr)
	print("Summation of All Elements is : ",Ret)

if __name__ == "__main__":
	main()
