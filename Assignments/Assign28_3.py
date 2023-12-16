# Write a program which accept one number from user and toggle 7th bit of that number. Return modified number. 

# Input : 137 
# Output : 201

# Num =  0000 0000 0000 0000 0000 0001 1101 0000
# Mask = 0000 0000 0000 0000 0000 0000 0100 0000
# Mask =  0    0    0    0    0    0    4    0
# Ans =  0000 0000 0000 0000 0000 0001 1001 0000

def ToggleBit(Value):
	Mask = 0x00000040

	Num = Value ^ Mask
	return Num

def main():
	No = int(input("Enter Number : "))

	Ret = ToggleBit(No)
	print("Modified Number is :",Ret)

if __name__ == "__main__":
	main()