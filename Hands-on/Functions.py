# 1 : Function fun accepts nothing and return nothing
def fun():
	print("Function fun")

# 2 : Function gun accepts 1 parameter and returns nothing
def gun(No):
	print("Function gun with parameter : ",No)

# 3 : Function sun accepts parameter and return the value
def sun(No):
	print("Function sun with parameter : ",No)
	return No+1

# 4 : Function AddSub accepts multiple values and return multiple values
def AddSub(No1,No2):
	Add = No1 + No2
	Sub = No1 - No2
	return Add,Sub

# 5 : Nested Function definition
def Python():
	print("Inside Python")
	def MachineLearning():
		print("Inside Machine Learning")
	MachineLearning()

# Entry - point function
def main():
	fun()
	gun(11)
	Ret = sun(10)
	print("Return value from sun is : ",Ret)

	Ret1,Ret2 = AddSub(12,10)
	print("Addition is : ",Ret1)
	print("Subtraction is : ",Ret2)

	Python()

# Code Starter
if __name__ == "__main__":
	main()