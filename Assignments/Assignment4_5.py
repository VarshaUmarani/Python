# Write a program which contains filter(), map() and reduce() in it.
# Python application which contains one list of numbers. List contains the numbers which are accepted from user. 
# Filter should filter out all prime numbers. 
# Map function will multiply each number by 2.
# Reduce will return Maximum number from that numbers.
# (You can also use normal functions instead of lambda functions). 

# Input List = [2, 70 , 11, 10, 17, 23, 31, 77] 
# List after filter = [2, 11, 17, 23, 31] 
# List after map = [4, 22, 34, 46, 62] 
# Output of reduce = 62

def CheckPrime(Num):
	Count = 0
	PrimeList = []

	for i in range(1,int(Num/2)+1):
		if Num % i == 0:
			Count = Count + 1
	
	if Count == 1:
		PrimeList.append(Num)

	return PrimeList

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
		No = int(input("Enter Element Number {} : ".format(i+1)))
		Arr.append(No)

	print("Entered List is : ",Arr)

	FilteredData = list(filter(CheckPrime,Arr))
	print("Filtered List is : ",FilteredData)

	MappedData = list(map((lambda No : No * 2),FilteredData))
	print("Mapped List is : ",MappedData)

	Output = Maximum(MappedData)
	print("Output of Reduce is : ",Output)

if __name__ == "__main__":
	main()