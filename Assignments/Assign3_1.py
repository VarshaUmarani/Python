# Write a program which accept one number from user and print that number of 
# even numbers on screen. 

# Input : 7 
# Output: 2 4 6 8 10 12 14

def DisplayEven(No):
	i = 1
	while i <= No:
		print(i*2,end = "  ")
		i = i + 1

def main():
	Num = int(input("Enter Number : "))

	DisplayEven(Num)

if __name__ == "__main__":
	main()