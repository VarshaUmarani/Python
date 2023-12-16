# Accept two numbers from user and display first number in second 
# number of times.

def DisplayPattern(No1,No2):
	for i in range(No2):
		print(No1,end = "  ")

def main():
	Num1 = int(input("Enter First Number : "))
	Num2 = int(input("Enter Second Number : "))

	DisplayPattern(Num1,Num2)

if __name__ == "__main__":
	main()