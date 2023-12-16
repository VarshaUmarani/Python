# Write a program which accept number from user and count frequency of such a 
# digits which are less than 6.

# Input : 2395 
# Output : 3 

# Input : 1018 
# Output : 3 

# Input : 9440 
# Output : 3 

# Input : 96672 
# Output : 1

def CountDigits(No):
	Digit = 0
	Cnt = 0

	while No != 0:
		Digit = No % 10
		if Digit < 6:
			Cnt = Cnt + 1
		No = int(No/10)

	return Cnt

def main():
	Num = int(input("Enter Number : "))

	Ret = CountDigits(Num)
	print("Count is :",Ret)

if __name__ == "__main__":
	main()