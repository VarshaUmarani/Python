# Write a program which accept accept range from user and display all numbers in 
# between that range in reverse order. 

# Input : 23 35 
# Output : 35 34 33 32 31 30 29 28 27 26 25 24 23 

# Input : 10 18 
# Output : 18 17 16 15 14 13 12 11 10 

# Input : 10 10 
# Output : 10 

# Input : -10 2 
# Output : 2 1 0 -1 -2 -3 -4 -5 -6 -7 -8 -9 -10 

# Input : 90 18 
# Output : Invalid range

def DisplayRange(No1,No2):
	if No1 > No2:
		print("Invalid Range...!!!")
		return

	for i in range(No2,(No1-1),-1):
		print(i,end = "  ")

def main():
	Value1 = int(input("Enter Starting Point : "))
	Value2 = int(input("Enter Ending Point : "))

	DisplayRange(Value1,Value2)

if __name__ == "__main__":
	main()