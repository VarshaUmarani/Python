# Write a program which accept one number from user and range of positions from user. Toggle all bits from that range. 

def Toggle_Bits(Value,start,end):
	Mask = 0x00000000
	Mask1 = 0x00000001
	Mask2 = 0x00000001

	Mask1 = (Mask1 << end) - 1
	Mask2 = (Mask2 << (start) - 1) - 1

	Mask = Mask1 ^ Mask2

	Num = Value ^ Mask
	return Num

def main():
	No = int(input("Enter Number : "))
	pos1 = int(input("Enter Starting Range : "))
	pos2 = int(input("Enter Ending Range : "))

	Ret = Toggle_Bits(No,pos1,pos2)
	print("Modified Number is :",Ret)

if __name__ == "__main__":
	main()