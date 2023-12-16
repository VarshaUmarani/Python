# Write a program which accept one number and position from user and check whether bit at that position is on or off. 
# If bit is one return TRUE otherwise return FALSE. 

# Input : 10 2 
# Output : TRUE

# Num =  0000 0000 0000 0000 0000 1100 0001 0001
# Mask = 0000 0000 0000 0000 0000 0000 0001 0001
# Mask =  0     0    0    0    0    0    0   F

def Check_Bit(Value,Pos):
	if Pos <= 0 or Pos > 32:
		print("Invalid Input...")
		return
		
	Mask = 0x00000001
	Mask = Mask << (Pos-1)

	Num = Value & Mask

	if Num == Mask:
		return True
	else:
		return False

def main():
	No = int(input("Enter Number : "))
	Pos = int(input("Enter Position : "))

	bRet = Check_Bit(No,Pos)
	if bRet == True:
		print("Bit is On")
	else:
		print("Bit is Off")

if __name__ == "__main__":
	main()