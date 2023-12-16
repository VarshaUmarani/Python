# Write a Python program to find the addition of these two numbers using Recursive function.

def Addition_Using_Recursion(No1,No2):
	if No2 == 0:
		return No1
	else:
		return Addition_Using_Recursion(No1+1,No2-1)

def main():
	Num1 = int(input("Enter First Number : "))
	Num2 = int(input("Enter Second Number : "))

	Result = Addition_Using_Recursion(Num1,Num2)
	print("Addition of {0} and {1} is : {2}".format(Num1,Num2,Result))

if __name__ == "__main__":
	main()