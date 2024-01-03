def Subtraction(Value1,Value2):
	if Value1 < Value2:
		Ret = Value2 - Value1
	else:
		Ret = Value1 - Value2
	return Ret

# Entry point function
def main():

	No1 = int(input("Enter First Number : "))
	No2 = int(input("Enter Second Number : "))

	Ans = Subtraction(No1,No2)
	print("Subtraction of {0} and {1} is : {2}".format(No1,No2,Ans))

if __name__ == "__main__":
	main()