# Write a program which accept number from user and count frequency of 4 in it. 

# Input : 2395 
# Output : 0 

# Input : 1018 
# Output : 0 

# Input : 9440 
# Output : 2 

# Input : 922432 
# Output : 1 

def CountFour(No):
	Cnt = 0
	Digit = 0

	while No != 0:
		Digit = No % 10
		if Digit == 4:
			Cnt = Cnt + 1
		No = int(No/10)

	return Cnt

def main():
	Num = int(input("Enter Number : "))

	Ret = CountFour(Num)
	print("Count of Four is :",Ret)

if __name__ == "__main__":
	main()