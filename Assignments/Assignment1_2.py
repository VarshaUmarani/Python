# Write a program which contains one function named as ChkNum() which accept one parameter as number. 
# If number is even then it should display “Even number” otherwise display “Odd number” on console.

# Input : 11
# Output : Odd Number

# Input : 8
# Output : Even Number

def CheckNumber(Value):
	if (Value % 2) == 0:
		return True
	else:
		return False

def main():
	Num = int(input("Enter any Number : "))

	Ret = CheckNumber(Num)

	if (Ret == True):
		print("{0} is Even Number".format(Num))
	else:
		print("{0} is Odd Number".format(Num))

if __name__ == "__main__":
	main()