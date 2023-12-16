import ArithmeticModule

def main():

	No1 = int(input("Enter First Number : "))
	No2 = int(input("Enter Second Number : "))

	Ans = ArithmeticModule.Addition(No1,No2)
	print("Addition of {0} and {1} is : {2}".format(No1,No2,Ans))

# __name__ -> is special variable
if __name__ == "__main__":
	main()