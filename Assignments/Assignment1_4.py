# Write a program which display 5 times Jay Ganesh...!!! on screen.

# Output :
# Jay Ganesh...!!!
# Jay Ganesh...!!!
# Jay Ganesh...!!!
# Jay Ganesh...!!!
# Jay Ganesh...!!!

def Display(Value):
	for i in range(Value):
		print("Jay Ganesh...!!!")

def main():
	No = int(input("Enter Number : "))

	Display(No)

if __name__ == "__main__":
	main()