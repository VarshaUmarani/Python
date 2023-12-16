def Division(Value1,Value2):
	if (Value2 != 0):
		Ret = Value1 / Value2
	else:
		return -1
	return Ret

# Entry point function
def main():

	No1 = int(input("Enter First Number : "))
	No2 = int(input("Enter Second Number : "))

	Ans = Division(No1,No2)
	if (Ans != -1):
		print("Division of {0} and {1} is : {2}".format(No1,No2,Ans))
	else:
		print("Division by 0 is not allowed")
		
if __name__ == "__main__":
	main()