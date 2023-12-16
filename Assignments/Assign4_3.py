# Write a program which accept number from user and display all its non factors. 

# Input : 12 
# Output : 5 7 8 9 10 11 

# Input : 13 
# Output : 2 3 4 5 6 7 8 9 10 11 12 

# Input : 10 
# Output : 3 4 6 7 8 9

def NonFactors(No):
	for i in range(1,No):
		if No % i != 0:
			print(i,end = "  ")

def main():
	Num = int(input("Enter Number : "))

	NonFactors(Num)

if __name__ == "__main__":
	main()