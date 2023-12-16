# Write a program which contains one function that accept one number from user and 
# returns true if number is divisible by 5 otherwise return false.

# Input : 8
# Output : False

# Input : 25
# Output : True

def CheckDivisible(Value):
	if (Value % 5) == 0:
		return True
	else:
		return False

def main():
	Num = int(input("Enter any Number : "))

	Ret = CheckDivisible(Num)

	if (Ret == True):
		print("Entered Number {0} is divisible by 5".format(Num))
	else:
		print("Entered Number {0} is not divisible by 5".format(Num))

if __name__ == "__main__":
	main()