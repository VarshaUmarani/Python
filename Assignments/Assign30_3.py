# Write a program which accept one number from user and check whether 9th or 12th bit is on or off. 

# Input : 257 
# Output : TRUE

# Num  = 0000 0000 0000 0000 0000 1001 0000 0100
# Mask = 0000 0000 0000 0000 0000 1001 0000 0000
# Ans  = 0000 0000 0000 0000 0000 1001 0000 0000

def Check_Bit(Value):
	Mask = 0x00000900

	Num  = Value & Mask

	if Num == Mask:
		return True
	else:
		return False

def main():
	No = int(input("Enter Number : "))

	bRet = Check_Bit(No)

	if bRet == True:
		print("TRUE")
	else:
		print("FALSE")

if __name__ == "__main__":
	main()