# Accept two Numbers from user and perform Addition and Subtraction of that numbers

# Definition of Addition function
def Addition(No1,No2):
	Ans = No1 + No2
	return Ans

# Definition of Subtraction function
def Subtraction(No1,No2):
	Ans = No1 - No2
	return Ans

# Entry Point Function
def main():
	print("Enter First Number : ")
	Value1 = int(input())

	print("Enter Second Number : ")
	Value2 = int(input())

	Ret1 = Addition(Value1,Value2)
	print("Addition is : ",Ret1)

	Ret2 = Subtraction(Value1,Value2)
	print("Subtraction is : ",Ret2)

# Code Starter
if __name__ == "__main__":
	main()