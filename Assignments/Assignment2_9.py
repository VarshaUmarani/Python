# Write a program which accept number from user and return number of digits in that number.

# Input : 5187934 
# Output : 7

def CountDigits(Num):
	Digit = 0
	Count = 0

	while Num != 0:
		Digit = Num % 10
		Num = int(Num / 10)
		Count = Count + 1

	return Count

def main():
	No = int(input("Enter Number : "))

	Ret = CountDigits(No)
	print("Count of Digits in {} is : {}".format(No,Ret))

if __name__ == "__main__":
	main()