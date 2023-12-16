# Write a program which accept number from user and return addition of digits in that number.

# Input : 5187934
# Output : 37

def SumDigits(No):
	Digit = 0
	Sum = 0

	while No != 0:
		Digit = No % 10
		Sum = Sum + Digit
		No = int(No / 10)

	return Sum

def main():
	Num = int(input("Enter Number : "))

	Ret = SumDigits(Num)
	print("Sum of Digits in {} is : {}".format(Num,Ret))

if __name__ == "__main__":
	main()