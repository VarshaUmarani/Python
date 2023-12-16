# Accept one number from user and print that number of * on screen. 

def PrintStar():
	print("*", end = "  ")

def DisplayPattern(No):
	Cnt = 0

	while Cnt < No:
		PrintStar()
		Cnt = Cnt + 1

def main():
	Num = int(input("Enter Number : "))

	DisplayPattern(Num)

if __name__ == "__main__":
	main()