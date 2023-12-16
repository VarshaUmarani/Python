# Accept N numbers from user and return difference between summation 
# of even elements and summation of odd elements. 

# Input : N : 6 
# Elements : 85 66 3 80 93 88 
# Output : 53 (234 - 181) 

def Accept(Size):
	Arr = []

	print("Enter Elements into list : ")
	for i in range(Size):
		Arr.append(int(input()))
	return Arr

def Difference(Arr):
	OddSum = 0
	EvenSum = 0
	for i in Arr:
		if i % 2 == 0:
			EvenSum = EvenSum + i
		else:
			OddSum = OddSum + i
	return EvenSum - OddSum

def main():
	Size = int(input("Enter Number of Elements : "))

	list = Accept(Size)

	Ret = Difference(list)
	print("Difference is :",Ret)

if __name__ == "__main__":
	main()