# Program to print 5 to 1 numbers on screen.

def DisplayPattern(No):
	for i in range(No,0,-1):
		print("Jay Shree Ram...!!! : {}".format(i))

def main():
	Num = int(input("Enter NUmber : "))

	DisplayPattern(Num)

if __name__ == "__main__":
	main()