# Write a program which accept number from user and print that number of “*” on screen.

# Input : 5
# Output : * * * * *

def Display(Value):
	for i in range(Value):
		print("*",end=" ")
	print()

def main():
	No = int(input("Enter Number : "))

	Display(No)

if __name__ == "__main__":
	main()