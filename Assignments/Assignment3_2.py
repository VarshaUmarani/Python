# Write a program which accept N numbers from user and store it into List. Return Maximum number from that List.

# Input : Number of elements : 7
# Input Elements : 13 5 45 7 4 56 34
# Output : 56

def Maximum(List):
	Max = 0

	for i in range(len(List)):
		if List[i] > Max:
			Max = List[i]

	return Max

def main():
	Arr = []

	Size = int(input("Enter Number of Elements : "))

	for i in range(Size):
		No = int(input("Enter Element at {} : ".format(i+1)))
		Arr.append(No)

	print("Entered Elements are : ",Arr)

	Ret = Maximum(Arr)
	print("Maximum Number from list is : ",Ret)

if __name__ == "__main__":
	main()