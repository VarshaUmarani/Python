# Write a program which accept number from user and return summation of all its non factors. 
# Input : 12 
# Output : 50 

# Input : 10 
# Output : 37

def SumofNonFactors(No):
	Sum = 0

	for i in range(1,No):
		if No % i != 0:
			Sum = Sum + i

	return Sum

def main():
	Num = int(input("Enter Number : "))

	Ret = SumofNonFactors(Num)
	print("Sum of Non Factors is :",Ret)

if __name__ == "__main__":
	main()