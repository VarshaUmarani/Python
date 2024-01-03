from Numbers import CheckEven

def main():
	print("Enter Number : ")
	No = int(input())

	bRet = CheckEven(No)

	if bRet == True:
		print("{} is Even Number".format(No))

	else:
		print("{} is Odd Number".format(No))

if __name__ == "__main__":
	main()