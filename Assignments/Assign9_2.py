# Write a program which accept range from user and display all even numbers in between that range. 

# Input : 23 35 
# Output : 24 26 28 30 32 34 

# Input : 10 18 
# Output : 10 12 14 16 18 

# Input : 10 10 
# Output : 10 

# Input : -10 2 
# Output : -10 -8 -6 -4 -2 0 2 

# Input : 90 18 
# Output : Invalid range 

def EvenRange(No1,No2):
	if No1 > No2:
		print("Invalid Range...!!!")
		return

	for i in range(No1,(No2+1)):
		if i % 2 == 0:
			print(i,end = "  ")

def main():
	Value1 = int(input("Enter Starting Point : "))
	Value2 = int(input("Enter Ending Point : "))

	EvenRange(Value1,Value2)

if __name__ == "__main__":
	main()