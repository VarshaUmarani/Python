# In built function from module
def Subtraction(no1,no2):
	return no1 - no2

# Function chaining
def SubDecorator(func_name,no1,no2):
	return func_name(no1,no2)			# Subtraction(no1,no2)

def main():
	num1 = int(input("Enter first number : "))
	num2 = int(input("Enter first number : "))

	ret = SubDecorator(Subtraction,num1,num2)
	print("Subtraction is : ",ret)

if __name__ == "__main__":
	main()