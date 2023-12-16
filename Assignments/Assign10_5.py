# Accept number from user and display below pattern. 

# Input : 8 
# Output : 2 4 6 8 10 12 14 16

def DisplayPattern(No):
	for i in range(1,No+1):
		print(i*2,end = "  ")

def main():
	Num = int(input("Enter Number : "))

	DisplayPattern(Num)

if __name__ == "__main__":
	main()