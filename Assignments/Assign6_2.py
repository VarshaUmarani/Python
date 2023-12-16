# Write a program which accept number from user and check whether it contains 0 in it or not. 

# Input : 2395 
# Output : There is no Zero 

# Input : 1018 
# Output : It Contains Zero 

# Input : 9000 
# Output : It Contains Zero 

# Input : 10687 
# Output : It Contains Zero

def CheckZero(No):
	Cnt = 0
	Digit = 0

	while No != 0:
		Digit = No % 10
		if Digit == 0:
			Cnt = Cnt + 1
		No = int(No/10)

	if Cnt != 0:
		return True
	else:
		return False

def main():
	Num = int(input("Enter Number : "))

	bRet = CheckZero(Num)
	if bRet == True:
		print("{} it contains Zero".format(Num))
	else:
		print("{} it doesn't contains Zero".format(Num))

if __name__ == "__main__":
	main()