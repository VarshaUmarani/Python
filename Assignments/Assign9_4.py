# Write a program which accept range from user and return addition of all even 
# numbers in between that range. (Range should contains positive numbers only) 

# Input : 23 30 
# Output : 108 

# Input : 10 18 
# Output : 70 

# Input : -10 2 
# Output : Invalid range 

# Input : 90 18 
# Output : Invalid range

def SumOfEvenRange(No1,No2):
	if No1 > No2 or No1 < 0 or No2 < 0:
		print("Invalid Range...!!!")
		return -1

	Sum = 0
	for i in range(No1,(No2+1)):
		if i % 2 == 0:
			Sum = Sum + i
	return Sum

def main():
	Value1 = int(input("Enter Starting Point : "))
	Value2 = int(input("Enter Ending Point : "))

	Ret = SumOfEvenRange(Value1,Value2)
	if Ret == -1:
		print()
	else:
		print("Addition is :",Ret)

if __name__ == "__main__":
	main()