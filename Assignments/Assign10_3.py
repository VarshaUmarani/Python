# Accept number from user and display below pattern. 

# Input : 5 
# Output : 1 * 2 * 3 * 4 * 5 * 

def DisplayPattern(No):
	for i in range(1,(No+1)):
		print("{} *".format(i), end = "  ")

def main():
	Value = int(input("Enter Number : "))

	DisplayPattern(Value)

if __name__ == "__main__":
	main()