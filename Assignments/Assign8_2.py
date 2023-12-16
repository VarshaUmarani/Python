# Write a program which accept number from user and print numbers till that number. 

# Input : 8 
# Output : 1 2 3 4 5 6 7 8 

def Display(No):
	if No < 0:
		No = -(No)

	for i in range(1,(No+1)):
		print(i,end = "  ")

def main():
	Num = int(input("Enter Number : "))

	Display(Num)

if __name__ == "__main__":
	main()