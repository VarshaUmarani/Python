# Write a program which accept N numbers from user and store it into List. Accept one another 
# number from user and return frequency of that number from List. 

# Input : Number of elements : 11 
# Input Elements : 13 5 45 7 4 56 5 34 2 5 65 
# Element to search : 5 
# Output : 3

def Frequency(List,Num):
	Count = 0

	for i in range(len(List)):
		if List[i] == Num:
			Count = Count + 1

	return Count

def main():
	Arr = []

	Size = int(input("Enter Number of Elements : "))

	for i in range(Size):
		No = int(input("Enter Element Number {} : ".format(i+1)))
		Arr.append(No)

	print("Entered Elements are : ",Arr)
	
	Value = int(input("Enter Element to Search : "))

	Ret = Frequency(Arr,Value)
	print("Frequency of {} in List is : {}".format(Value,Ret))

if __name__ == "__main__":
	main()