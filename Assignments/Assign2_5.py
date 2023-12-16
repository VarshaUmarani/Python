# Accept number from user and check whether number is even or odd.

def CheckNumber(No):
	if No % 2 == 0:
		return True
	else:
		return False

def main():
	Num = int(input("Enter Number : "))

	bRet = CheckNumber(Num)
	if bRet == True:
		print("{} is Even".format(Num))
	else:
		print("{} is Odd".format(Num))

if __name__ == "__main__":
	main()