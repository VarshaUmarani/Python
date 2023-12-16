# Write a program which accept one number from user and on its first 4 bits. Return modified number. 

# Input : 73 
# Output : 79

# Num =  0000 0000 0000 0000 0000 1100 0001 0000
# Mask = 0000 0000 0000 0000 0000 0000 0000 1111
# Mask =  0     0    0    0    0    0    0   F

def OnBits(Num):
	Mask = 0x0000000F

	Value = Num | Mask
	return Value

def main():
	No = int(input("Enter Number : "))

	Ret = OnBits(No)
	print("Modified Number is :",Ret)

if __name__ == "__main__":
	main()