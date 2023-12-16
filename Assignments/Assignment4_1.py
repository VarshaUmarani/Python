# Write a program which contains one lambda function which accepts one parameter and return power of two. 

# Input : 4
# Output : 16 

# Input : 6
# Output : 36

PowerofTwo = lambda Num : Num ** 2

def main():
	No =int(input("Enter Number : "))

	Ret = PowerofTwo(No)
	print("Square of {} is : {}".format(No,Ret))

if __name__ == "__main__":
	main()