# Write a program which accept one number from user and toggle 7th and 10th bit of that number. Return modified number. 

# Input : 137 
# Output : 713 

# Num =  0000 0000 0000 0000 0000 0001 1101 0000
# Mask = 0000 0000 0000 0000 0000 0010 0100 0000
# Mask =  0    0    0    0    0    2    4    0
# Ans =  0000 0000 0000 0000 0000 0001 1001 0000

def ToggleBits(Value):
	Mask = 0x00000240

	Num = Value ^ Mask
	return Num

def main():
	No = int(input("Enter Number : "))

	Ret = ToggleBits(No)
	print("Modified Number is :",Ret)

if __name__ == "__main__":
	main()