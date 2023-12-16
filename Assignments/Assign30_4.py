# Write a program which accept one number , two positions from user and check whether bit at first or bit at second position is ON or OFF. 

# Input : 10 3 7 
# Output : TRUE 

# Num  = 0000 0000 0000 0000 0000 1001 0000 0100
# Mask = 0000 0000 0000 0000 0000 1001 0000 0000
# Ans  = 0000 0000 0000 0000 0000 1001 0000 0000

def Check_Bit(Value,pos1,pos2):
	Mask = 0x00000001

	Mask1 = Mask << (pos1 - 1)
	Mask2 = Mask << (pos2 - 1)

	Mask = Mask1 | Mask2

	Num  = Value & Mask

	if Num == Mask:
		return True
	else:
		return False

def main():
	No = int(input("Enter Number : "))
	Pos1 = int(input("Enter First Position : "))
	Pos2 = int(input("Enter Second Position : "))

	bRet = Check_Bit(No,Pos1,Pos2)

	if bRet == True:
		print("TRUE")
	else:
		print("FALSE")

if __name__ == "__main__":
	main()