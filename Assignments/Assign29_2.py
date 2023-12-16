# Write a program which accept one number and position from user and off that bit. Return modified number. 

# Input : 10 2 
# Output : 8

# Num =  0000 0000 0000 0000 0000 0000 0000 1010
# Mask = 1111 1111 1111 1111 1111 1111 1111 1111
# Mask =  0     0    0    0    0    0    0   F

def Off_Bit(Value,Pos):
	if Pos <= 0 or Pos > 32:
		print("Invalid Input...")
		return
		
	Mask = 0x00000001
	Mask = Mask << (Pos-1)
	Mask = ~Mask

	Num = Value & Mask
	return Num

def main():
	No = int(input("Enter Number : "))
	Pos = int(input("Enter Position : "))

	Ret = Off_Bit(No,Pos)
	print("Modified Number is :",Ret)

if __name__ == "__main__":
	main() 