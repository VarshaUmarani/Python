# Write a program which contains one lambda function which accepts two parameters and return its multiplication. 

# Input : 4 3
# Output : 12 

# Input : 6 3 
# Output : 18

Multiplication = lambda Num1,Num2 : Num1 * Num2

def main():
	Value1 = int(input("Enter First Number : "))
	Value2 = int(input("Enter Second Number : "))

	Ret = Multiplication(Value1,Value2)
	print("Multiplication of {} and {} is : {}".format(Value1,Value2,Ret))

if __name__ == "__main__":
	main()