# Write a program which checks whether 7th & 15th & 21st , 28th bit is On or OFF.

# Mask = 	0000 1000 0001 0000 0100 0000 0100 0000
# 			 0    8    1    0    4    0    4    0

def Check_Bit(Num):
	Mask = 0x08104040

	Result = Num & Mask

	if Result == Mask:
		return True
	else:
		return False

def main():
	No = int(input("Enter Number : "))

	bRet = Check_Bit(No)
	if bRet == True:
		print("7th, 15th, 21st & 28th Bits are ON")
	else:
		print("One of the 7th, 15th, 21st or 28th Bits are Off")

if __name__ == "__main__":
	main()