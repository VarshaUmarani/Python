# Write a program which accept number from user and print factors of that number. 

# Input : 24 
# Output: 1 2 4 6 8 12

def DisplayFactors(No):
	for i in range(1,int(No/2)+1):
		if No % i == 0:
			print(i, end = "  ")

def main():
	Num = int(input("Enter Number : "))

	DisplayFactors(Num)

if __name__ == "__main__":
	main()