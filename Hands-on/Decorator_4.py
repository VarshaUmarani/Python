# In built function from module
def Subtraction(no1,no2):
	return no1 - no2

# Function chaining
def SubDecorator(func_name):
	def Updater(no1,no2):
		if no1 < no2:				# If no1 is smaller than no2
			no1, no2 = no2, no1		# Swapping
		return func_name(no1,no2)

	return Updater

def main():
	Sub = SubDecorator(Subtraction)		# Sub = Updater

	num1 = int(input("Enter first number : "))
	num2 = int(input("Enter first number : "))

	# ret = Updater(num1,num2)
	ret = Sub(num1,num2)
	print("Subtraction is : ",ret)

if __name__ == "__main__":
	main()

# Function flow ->
# 24 -> 25 -> 14 - 15 -> 6 -> 12 -> 15 -> Sub = Updater
# # 16, 17, 18, 19,20, 21 -> ret = Updater(num1,num2) -> 7 -> 8,9,10 -> 21 ->  22 -> 25 -> End