# Named Function
def Addition(No1,No2):
	Ans = No1 + No2
	return Ans

# Lambda Function
# Name = lambda parameters : Body (Expression)
Sum = lambda No1,No2 : No1 + No2

def fun(Name):
	print("Enter First Number : ")
	Value1 = int(input())

	print("Enter Second Number : ")
	Value2 = int(input())

	Ret = Name(Value1,Value2)
	print("Value from fun is :",Ret)

def main():
	print("Enter First Number : ")
	Value1 = int(input())

	print("Enter Second Number : ")
	Value2 = int(input())

	Ret = Addition(Value1,Value2)
	print("Addition is :",Ret)

	Ret = Sum(Value1,Value2)
	print("Addition of lambda function is :",Ret)

	# Both give same output.
	fun(Sum)
	fun(Addition)

if __name__ == "__main__":
	main()