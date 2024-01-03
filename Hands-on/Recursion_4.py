# Accept one number from user and perform addition of numbers between 0 and that particular number.

# Input : 5
# Output : 5 + 4 + 3 + 2 + 1 = 15

# Global Variable Definition
Sum = 0

def Recursion(No):
	# Variable Declaration
	global Sum
	if No != 0:
		Sum = Sum + No
		No = No - 1
		Recursion(No)

	return Sum

def main():
	Value = int(input("Enter Number : "))

	Ret = Recursion(Value)
	print("Summation of Number is : ",Ret)

if __name__ == "__main__":
	main()