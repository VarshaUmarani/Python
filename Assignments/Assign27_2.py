# Write a program which checks whether 5th & 18th bit is On or OFF.

# Mask = 	0000 0000 0000 0010 0000 0000 0001 0000
# 			 0    0    0    2    0    0    1    0

def Check_Bit(Num):
	Mask = 0x00020010

	Result = Num & Mask

	if Result == Mask:
		return True
	else:
		return False

def main():
	No = int(input("Enter Number : "))

	bRet = Check_Bit(No)
	if bRet == True:
		print("5th & 18th Bits are ON")
	else:
		print("One of the 5th or 18th Bits are Off")

if __name__ == "__main__":
	main()