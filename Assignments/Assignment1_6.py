# Write a program which accept number from user and check whether that number is positive or negative or zero.

# Input : 11
# Output : Positive Number

# Input : -8
# Output : Negative Number

# Input : 0
# Output : Zero

def CheckNumber(Value):
	if Value == 0:
		return -1
	elif Value > 0:
		return True
	else:
		return False

def main():
	No = int(input("Enter Number to Check : "))

	Ret = CheckNumber(No)

	if Ret == True:
		print("{0} is Positive Number".format(No))
	elif Ret == False:
		print("{0} is Negative Number".format(No))
	else:
		print("Entered Number is Zero")

if __name__ == "__main__":
	main()