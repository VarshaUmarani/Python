# Write a program which accept number from user and display its multiplication of factors. 

# Input : 12 
# Output : 144 (1 * 2 * 3 * 4 * 6) 

# Input : 13 
# Output : 1 (1) 

# Input : 10 
# Output : 10 (1 * 2 * 5)

def MultFactors(No):
	Mult = 1
	for i in range(1,int(No/2)+1):
		if No % i == 0:
			Mult = Mult * i

	return Mult

def main():
	Num = int(input("Enter Number : "))

	Ret = MultFactors(Num)
	print("Multiplication of Factors is :",Ret)

if __name__ == "__main__":
	main()