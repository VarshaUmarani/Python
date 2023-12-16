# Write a program which accept one number from user and off 7th and 10th bit of that number. Return modified number. 

# Input : 577 
# Output : 1

# Num =  0000 0000 0000 0000 0000 0011 1101 0000
# Mask = 1111 1111 1111 1111 1111 1101 1011 1111
# Mask =  F    F    F    F    F    D    B   F
# Ans =  0000 0000 0000 0000 0000 0001 1001 0000

def OffBits(Value):
	Mask = 0xFFFFFDBF

	Num = Value & Mask
	return Num

def main():
	No = int(input("Enter Number : "))

	Ret = OffBits(No)
	print("Modified Number is :",Ret)

if __name__ == "__main__":
	main()