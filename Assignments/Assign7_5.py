# Write a program which accept number from user and return difference between 
# summation of even digits and summation of odd digits. 

# Input : 2395 
# Output : -15 (2 - 17) 

# Input : 1018 
# Output : 6 (8 - 2) 

# Input : 8440 
# Output : 16 (16 - 0) 

# Input : 5733 
# Output : -18 (0 - 18)

def CountDifference(No):
	Odd = 0
	Even = 0
	Digit = 0

	while No != 0:
		Digit = No % 10
		if Digit % 2 == 0:
			Even = Even + Digit
		else:
			Odd = Odd + Digit
		No = int(No/10)

	return Even - Odd

def main():
	Num = int(input("Enter Number : "))

	Ret = CountDifference(Num)
	print("Difference is :",Ret)

if __name__ == "__main__":
	main()