# Accept one number from user and calculate factorial of that number.

# Global Variable Definition
fact = 1

def Factorial(No):
	# Global Variable Declaration
	global fact
	if No != 0:
		fact = fact * No
		No = No - 1
		Factorial(No)

	return fact

def main():
	Value = int(input("Enter Number to Check Factorial : "))

	Ret = Factorial(Value)
	print("Factorial of {} is : {}".format(Value,Ret))

if __name__ == "__main__":
	main()