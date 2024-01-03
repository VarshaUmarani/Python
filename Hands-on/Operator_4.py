# Implementation of Operator overloading.

class Demo:
	def __init__(self,x,y):
		self.i = x
		self.j = y

	def __add__(self,other):
		no1 = self.i + other.i
		no2 = self.j + other.j
		return Demo(no1,no2)
		# return Demo(self.i + other.i,self.j + other.j)

def main():
	no1 = int(input("Enter first number : "))
	no2 = int(input("Enter second number : "))
	obj1 = Demo(no1,no2)

	no1 = int(input("Enter first number : "))
	no2 = int(input("Enter second number : "))
	obj2 = Demo(no1,no2)

	ret = obj1 + obj2	# obj1.__add__(obj2) -> __add__(obj1,obj2)
	print(ret.i,ret.j)

if __name__ == "__main__":
	main()