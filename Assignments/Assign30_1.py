# Write a program which accept one number from user and count number of ON (1) bits in it without using % and / operator.

# Input : 11 
# Output : 3

def Count_ON_Bits(Value):
	Mask = 0x00000001
	Pos = 1
	Cnt = 0

	while Pos != 32:
		Num = Value & Mask
		if Num == Mask:
			Cnt = Cnt + 1
		Mask = Mask << 1
		Pos = Pos + 1
	return Cnt

def main():
	No = int(input("Enter Number : "))

	Ret = Count_ON_Bits(No)
	print("Count of ON Bits is :",Ret)

if __name__ == "__main__":
	main()