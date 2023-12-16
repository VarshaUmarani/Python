# Write a program which checks whether first and last bit is On or OFF. 
# First bit means bit number 1 and last bit means bit number 32.

# Mask = 	1000 0000 0000 0000 0000 0000 0000 0001
# 			 8    0    0    0    0    0    0    1

def Check_Bit(Num):
	Mask = 0x80000001

	Result = Num & Mask

	if Result == Mask:
		return True
	else:
		return False

def main():
	No = int(input("Enter Number : "))

	bRet = Check_Bit(No)
	if bRet == True:
		print("First and Last Bits are ON")
	else:
		print("One of the First and Last Bits are Off")

if __name__ == "__main__":
	main()