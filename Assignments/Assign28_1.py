# Write a program which accept one number from user and off 7th bit of that number if it is on. Return modified number. 

# Input : 79 
# Output : 15

# Num =  0000 0000 0000 0000 0000 0001 1101 0000
# Mask = 1111 1111 1111 1111 1111 1111 1011 1111
# Mask =  F    F    F    F    F    F    B   F
# Ans =  0000 0000 0000 0000 0000 0001 1001 0000

def OffBit(Value):
	Mask = 0xFFFFFFBF

	Num = Value & Mask
	return Num

def main():
	No = int(input("Enter Number : "))

	Ret = OffBit(No)
	print("Modified Number is :",Ret)

if __name__ == "__main__":
	main()