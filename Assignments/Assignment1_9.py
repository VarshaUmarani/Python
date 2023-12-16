# Write a program which display first 10 even numbers on screen.
# Output : 2 4 6 8 10 12 14 16 18 20

def Display(Value):
	for i in range(1,Value+1):
		print(i*2,end=" ")
	print()

def main():
	No = int(input("Enter Number : "))

	Display(No)

if __name__ == "__main__":
	main()