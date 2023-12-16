# Write a program which accept range from user and return addition of all numbers 
# in between that range. (Range should contains positive numbers only) 

# Input : 23 30 
# Output : 212 

# Input : 10 18 
# Output : 126 

# Input : -10 2 
# Output : Invalid range 

# Input : 90 18 
# Output : Invalid range

def RangeSum(No1,No2):
	if No1 > No2 or No1 < 0 or No2 < 0:
		print("Invalid Range...!!!")
		return -1

	Sum = 0
	for i in range(No1,(No2+1)):
		Sum = Sum + i
	return Sum

def main():
	Value1 = int(input("Enter Starting Point : "))
	Value2 = int(input("Enter Ending Point : "))

	Ret = RangeSum(Value1,Value2)
	if Ret == -1:
		print()
	else:
		print("Sum of All Numbers in range is :",Ret)

if __name__ == "__main__":
	main()