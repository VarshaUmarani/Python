# Write a program which accept number from user and display its factors in 
# decreasing order.

# Input : 12 
# Output : 6 4 3 2 1

# Input : 13 
# Output : 1 

# Input : 10 
# Output : 5 2 1

def FactorsReverse(No):
	for i in range(int(No/2),0,-1):
		if No % i == 0:
			print(i,end = "  ")

def main():
	Num = int(input("Enter Number : "))

	FactorsReverse(Num)

if __name__ == "__main__":
	main()