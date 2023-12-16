# Write a program which accept two numbers from user and display position of common ON bits from that two numbers. 

# Input : 10 15 (1010 1111) 
# Output : 2 4 

def Display_Common_OnBits(Value1,Value2):
	Mask = 0x00000001
	Pos = 1

	while Pos != 32:
		Num1 = Value1 & Mask
		Num2 = Value2 & Mask

		if Num1 == Mask and Num2 == Mask:
			print(Pos,end = "  ")

		Pos = Pos + 1
		Mask = Mask << 1

def main():
	No1 = int(input("Enter First Number : "))
	No2 = int(input("Enter Second Number : "))

	Display_Common_OnBits(No1,No2)

if __name__ == "__main__":
	main()