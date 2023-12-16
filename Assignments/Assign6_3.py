# Write a program which accept number from user and count frequency of 2 in it. 

# Input : 2395 
# Output : 1 

# Input : 1018 
# Output : 0 

# Input : 9000 
# Output : 0 

# Input : 922432 
# Output : 3

def CountTwo(No):
	Digit = 0
	Cnt = 0

	while No != 0:
		Digit = No % 10
		if Digit == 2:
			Cnt = Cnt + 1
		No = int(No/10)

	return Cnt

def main():
	Num = int(input("Enter Number : "))

	Ret = CountTwo(Num)
	print("Count of two is :",Ret)

if __name__ == "__main__":
	main()