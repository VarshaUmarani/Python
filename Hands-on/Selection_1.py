# Demonstration of Selection

def CheckEven(Num):
	if Num % 2 == 0:
		return True
	else:
		return False

def main():
	No = int(input("Enter Number : "))

	Ret = CheckEven(No)
	if Ret == True:
		print("{} is Even Number".format(No))
	else:
		print("{} is Odd Number".format(No))

if __name__ == "__main__":
	main()