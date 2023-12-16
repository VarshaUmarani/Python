# Write a program which accept one number from user and return its factorial.

# Input : 5
# Output : 120

def Factorial(Num):
	Fact = 1
	while Num != 0:
		Fact = Fact * Num
		Num = Num - 1

	return Fact

def main():
	No = int(input("Enter Number to find Factorial : "))

	Ret = Factorial(No)
	print("Factorial of {} is : {}".format(No,Ret))

if __name__ == "__main__":
	main()