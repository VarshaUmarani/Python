# Write a Python program to find the addition of these two numbers. 

def Addition(No1,No2):
	Addition = No1 + No2
	return Addition

def main():
	Num1 = int(input("Enter First Number : "))
	Num2 = int(input("Enter Second Number : "))

	Result = Addition(Num1,Num2)
	print("Addition of {0} and {1} is : {2}".format(Num1,Num2,Result))

if __name__ == "__main__":
	main()