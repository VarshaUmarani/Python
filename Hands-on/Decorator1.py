# The concept of Decorator is not used here.

# In built function from module
def Subtraction(no1,no2):
	return no1 - no2

def main():
	num1 = int(input("Enter first number : "))
	num2 = int(input("Enter first number : "))

	ret = Subtraction(num1,num2)
	print("Subtraction is : ",ret)

if __name__ == "__main__":
	main()