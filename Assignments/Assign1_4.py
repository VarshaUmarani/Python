# Accept one number and check whether is is divisible by 5 or not.

def CheckDivisible(Dividend,Divisor):
	if Dividend == 0:
		return -1
	else:
		Quotient = Dividend % Divisor
		if Quotient == 0:
			return True
		else:
			return False

def main():
	Dividend = int(input("Enter Dividend : "))
	Divisor = int(input("Enter Divisor : "))

	bRet = CheckDivisible(Dividend,Divisor)
	if bRet == True:
		print("{} is Divisible by {}".format(Dividend,Divisor))
	else:
		print("{} is not Divisible by {}".format(Dividend,Divisor))

if __name__ == "__main__":
	main()