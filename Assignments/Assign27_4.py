# Write a program which checks whether 7th & 8th & 9th bit is On or OFF.

# Mask = 	0000 0000 0000 0000 0000 0001 1100 0000
# 			 0    0    0    0    0    1    C    0

def Check_Bit(Num):
	Mask = 0x000001C0

	Result = Num & Mask

	if Result == Mask:
		return True
	else:
		return False

def main():
	No = int(input("Enter Number : "))

	bRet = Check_Bit(No)
	if bRet == True:
		print("7th, 8th & 9th Bits are ON")
	else:
		print("One of the 7th, 8th or 9th Bits are Off")

if __name__ == "__main__":
	main()