# Write a program which contains one function named as Add() which accepts two numbers
# from user and return addition of that two numbers.

# Input : 11 5
# Output : 16

def Addition(Value1,Value2):
	Ret = Value1 + Value2
	return Ret

def main():
	No1 = int(input("Enter First Number : "))
	No2 = int(input("Enter Second Number : "))

	Ans = Addition(No1,No2)
	print("Addition of {0} and {1} is : {2}".format(No1,No2,Ans))

if __name__ == "__main__":
	main()