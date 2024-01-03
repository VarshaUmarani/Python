# Demonstration of Inheritance
# Multiple inheritance

class Base1:
	def __init__(self):
		self.no1 = 10
		self.no2 = 20
		print("Inside Base1 __init__ method.!")

	def fun(self):
		print("Inside Base1 fun.!")

class Base2:			
	def __init__(self):
		self.num1 = 300
		self.num2 = 40
		print("Inside Base2 __init__ method.!")

	def fun(self):
		print("Inside Base2 fun.!")

class Derived(Base1,Base2):				# Multiple inheritance
	def __init__(self):
		Base1.__init__(self)
		Base2.__init__(self)
		self.Value1 = 50
		self.Value2 = 60
		print("Inside Derived __init__ method.!")

	def gun(self):
		print("Inside Derived sun.!")

def main():

	dobj = Derived()	# Object of Derived1 class

	dobj.fun()			# Base1 fun() bcz of 22th statement as Base1 is first derived
	dobj.gun()			# Derived gun()

if __name__ == "__main__":
	main()