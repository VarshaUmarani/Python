# Write a program which display 10 to 1 on screen.
# Output : 10 9 8 7 6 5 4 3 2 1

def Display(Value):
	for i in range(Value,0,-1):
		print(i,end=" ")
	print()

def main():
	No = int(input("Enter Number : "))

	Display(No)

if __name__ == "__main__":
	main()