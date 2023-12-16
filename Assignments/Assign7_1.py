# Write a program which accept number from user and return the count of even digits. 

# Input : 2395 
# Output : 1 

# Input : 1018 
# Output : 2 

# Input : -1018 
# Output : 2 

# Input : 8462 
# Output : 4

def CountEven(No):
	Digit = 0
	Cnt = 0

	if No < 0:
		No = -(No)

	while No != 0:
		Digit = No % 10
		if Digit % 2 == 0:
			Cnt = Cnt + 1
		No = int(No/10)

	return Cnt

def main():
	Num = int(input("Enter Number : "))

	Ret = CountEven(Num)
	print("Count of Even Digits is :",Ret)

if __name__ == "__main__":
	main()