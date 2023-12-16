# Write a program which accept number from user and return difference between 
# summation of all its factors and non factors. 

# Input : 12 
# Output : -34 (16 - 50) 

# Input : 10 
# Output : -29 (8 - 37)

def FactorsDiff(No):
	Fact = 0
	NonFact = 0

	for i in range(1,No):
		if No % i == 0:
			Fact = Fact + i
		else:
			NonFact = NonFact + i

	return Fact - NonFact

def main():
	Num = int(input("Enter Number : "))

	Ret = FactorsDiff(Num)
	print("Difference is :",Ret)

if __name__ == "__main__":
	main()