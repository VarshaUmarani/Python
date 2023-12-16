# Write a program which accept number from user and print that number of $ & * on screen. 

# Input : 5 
# Output : $ * $ * $ * $ * $ * 

# Input : 3 
# Output : $ * $ * $ * 

# Input : -3 
# Output : $ * $ * $ * 

def Print():
	print("$  *",end = "  ")

def DisplayPattern(No):
	if No < 0:
		No = -(No)
		
	for i in range(No):
		Print()

def main():
	Num = int(input("Enter Number : "))

	DisplayPattern(Num)

if __name__ == "__main__":
	main()