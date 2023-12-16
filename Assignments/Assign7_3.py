# Write a program which accept number from user and return the count of digits in between 3 and 7. 

# Input : 2395 
# Output : 1 

# Input : 1018 
# Output : 0 

# Input : 4521 
# Output : 2 

# Input : 9922 
# Output : 0

def CountRange(No):
	Cnt = 0
	Digit = 0

	while No != 0:
		Digit = No % 10
		if Digit > 3 and Digit < 7:
			Cnt = Cnt + 1
		No = int(No/10)

	return Cnt

def main():
	Num = int(input("Enter Number : "))

	Ret = CountRange(Num)
	print("Count is :",Ret)

if __name__ == "__main__":
	main()