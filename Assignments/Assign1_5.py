# Accept one number from user and print that number of * on screen. 

def PrintStar():
	print("*",end = " ")

def DisplayStar(No):
	for i in range(No):
		PrintStar()

def main():
	Num = int(input("Enter Number : "))

	DisplayStar(Num)

if __name__ == "__main__":
	main()