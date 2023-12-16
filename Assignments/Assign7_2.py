# Write a program which accept number from user and return the count of odd digits. 

# Input : 2395
# Output : 3 

# Input : 1018 
# Output : 2 

# Input : -1018 
# Output : 2 

# Input : 8462 
# Output : 0

def CountOdd(No):
	Cnt = 0
	Digit = 0

	if No < 0:
		No = -(No)

	while No != 0:
		Digit = No % 10
		if Digit % 2 != 0:
			Cnt = Cnt + 1
		No = int(No / 10)

	return Cnt

def main():
	Num = int(input("Enter Number : "))

	Ret = CountOdd(Num)
	print("Count of Odd digits is :",Ret)

if __name__ == "__main__":
	main()