# Write a program which accept number from user and return multiplication of all digits. 

# Input : 2395 
# Output : 270 

# Input : 1018 
# Output : 8 

# Input : 9440 
# Output : 144 

# Input : 922432 
# Output : 864

def MultDigits(No):
	Mult = 1
	Digit = 0

	while No != 0:
		Digit = No % 10
		if Digit != 0:
			Mult = Mult * Digit
		No = int(No/10)

	return Mult

def main():
	Num = int(input("Enter Number : "))

	Ret = MultDigits(Num)
	print("Multiplication of all digits is :",Ret)

if __name__ == "__main__":
	main()