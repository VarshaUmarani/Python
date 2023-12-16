# Write a program which accept N numbers from user and store it into List. Return Minimum number from that List. 

# Input : Number of elements : 4 
# Input Elements : 13 5 45 7 
# Output : 5

def Minimum(List):
	Min = List[0]

	for i in range(len(List)):
		if List[i] < Min:
			Min = List[i]

	return Min

def main():
	Arr = []

	Size = int(input("Enter Number of Elements : "))

	for i in range(Size):
		No = int(input("Enter Element at {} : ".format(i+1)))
		Arr.append(No)

	print("Entered Elements are : ",Arr)

	Ret = Minimum(Arr)
	print("Minimum Number from list is : ",Ret)

if __name__ == "__main__":
	main()