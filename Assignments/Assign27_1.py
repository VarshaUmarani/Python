# Write a program which checks whether 15th bit is On or OFF.

# Mask = 	0000 0000 0000 0000 0100 0000 0000 0000
# 			 0    0    0    0    4    0    0    0

def Check_Bit(Num):
	Mask = 0x00004000

	Result = Num & Mask

	if Result == Mask:
		return True
	else:
		return False

def main():
	No = int(input("Enter Number : "))

	bRet = Check_Bit(No)
	if bRet == True:
		print("15th Bit is ON")
	else:
		print("15th Bit is Off")

if __name__ == "__main__":
	main()