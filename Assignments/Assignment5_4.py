# Write a recursive program which accept number from user and return summation of its digits. 

# Input : 879 
# Output : 24 

Digit = 0
Sum = 0

def SumofDigits(Num):
	global Digit
	global Sum

	if Num != 0:
		Digit = Num % 10
		Sum = Sum + Digit
		Num = int(Num / 10)
		SumofDigits(Num)

	return Sum

def main():
	Value = int(input("Enter Number : "))

	Ret = SumofDigits(Value)
	print("Summation of Digits in {} is : {}".format(Value,Ret))

if __name__ == "__main__":
	main()