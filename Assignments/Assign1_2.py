# Program to print 5 times “Jay Ganesh...!!!” on screen.

def DisplayPattern(No):
	for i in range(No):
		print("Jay Ganesh...!!!")

def main():
	Num = int(input("Enter the Number : "))

	DisplayPattern(Num)

if __name__ == "__main__":
	main()