# Write a program which accept N numbers from user and store it into List. Return addition of all elements from that List. 

# Input : Number of elements : 6 
# Input Elements : 13 5 45 7 4 56 
# Output : 130

def Summation(List):
	Sum = 0
	for i in range(len(List)):
		Sum = Sum + List[i]

	return Sum

def main():
	Arr = []

	Size = int(input("Enter Number of Elements : "))

	for i in range(Size):
		No = int(input("Enter Element at {} : ".format(i+1)))
		Arr.append(No)

	print("Entered Elements are : ",Arr)

	Ret = Summation(Arr)
	print("Addition of all the Elements is : ",Ret)

if __name__ == "__main__":
	main()