# Write a program which accept N and print first 10 multiples of N. 

# Input : 4 
# Output : 4 8 12 16 20

def Display(No):
	i = 1

	while i <= 10:
		print(i*No,end = "  ")
		i = i + 1

def main():
	Num = int(input("Enter Number : "))

	Display(Num)

if __name__ == "__main__":
	main()