# Write a recursive program which accept number from user and return its factorial. 

# Input : 5 
# Output : 120

Fact = 1

def Factorial(Num):
	global Fact

	if Num != 0:
		Fact = Fact * Num
		Num = Num - 1
		Factorial(Num)

	return Fact

def main():
	No = int(input("Enter Number : "))

	Ret = Factorial(No)
	print("Factorial of {} is : {}".format(No,Ret))

if __name__ == "__main__":
	main()