# Accept one number from user and print that number of * on screen.

def PrintStar():
	print("*",end = "  ")

def DisplayPattern(No):
	for i in range(No):
		PrintStar()

def main():
	Num = int(input("Enter Number : "))

	DisplayPattern(Num)

if __name__ == "__main__":
	main()