# Implementation of Addition function in Object Oriented Way

class Demo:
	def __init__(self,x,y):
		self.i = x
		self.j = y

	def Addition(self):
		return self.i + self.j

def main():
	no1 = int(input("Enter first number : "))
	no2 = int(input("Enter second number : "))

	obj1 = Demo(no1,no2)
	ret = obj1.Addition()
	print("Addition is : ",ret)

	no1 = int(input("Enter first number : "))
	no2 = int(input("Enter second number : "))

	obj2 = Demo(no1,no2)
	ret = obj2.Addition()
	print("Addition is : ",ret)

if __name__ == "__main__":
	main()