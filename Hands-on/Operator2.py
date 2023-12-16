# Implementation of Operator overloading.

class Demo:
	def __init__(self,x,y):
		self.i = x
		self.j = y

def main():
	no1 = int(input("Enter first number : "))
	no2 = int(input("Enter second number : "))
	obj1 = Demo(no1,no2)

	no1 = int(input("Enter first number : "))
	no2 = int(input("Enter second number : "))
	obj2 = Demo(no1,no2)

	# TypeError: unsupported operand type(s) for +: 'Demo' and 'Demo'
	# ret = obj1 + obj2	

if __name__ == "__main__":
	main()