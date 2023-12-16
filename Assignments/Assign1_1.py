# Program to divide two numbers.

def Division(No1,No2):
	if No2 == 0:
		return -1
	elif No1 > No2:
		return int(No1 / No2)
	else:
		return int(No2 / No1)

def main():
	Num1 = int(input("Enter First Number : "))
	Num2 = int(input("Enter Second Number : "))

	Ret = Division(Num1,Num2)
	print("Division is :",Ret)

if __name__ == "__main__":
	main()