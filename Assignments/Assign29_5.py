# Write a program which accept one number from user and toggle contents of first and last nibble of the number.
# Return modified number. (Nibble is a group of four bits)

# Num  = 0000 0000 0000 0110 0000 0000 0000 1111
# Mask = 1111 0000 0000 0000 0000 0000 0000 1111
# Ans  = 0000 0000 0000 0000 0000 0000 0000 0000

def Toggle_Bits(Value):
	Mask = 0xF000000F

	Num = Value ^ Mask
	return Num

def main():
	No = int(input("Enter Number : "))

	Ret = Toggle_Bits(No)
	print("Modified Number is :",Ret)

if __name__ == "__main__":
	main()