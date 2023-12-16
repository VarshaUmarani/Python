# Demonstration of Inheritance
# Multiple inheritance

class Base1:
	def __init__(self):
		self.no1 = 10
		self.no2 = 20
		print("Inside Base1 __init__ method.!")

	def fun(self):
		print("Inside Base1 fun.!")

	def gun(self):
		print("Inside Base1 gun.!")

class Base2:			
	def __init__(self):
		self.num1 = 30
		self.num2 = 40
		print("Inside Base2 __init__ method.!")

	def gun(self):
		print("Inside Base2 gun.!")

class Derived(Base1,Base2):				# Multiple inheritance
	def __init__(self):
		Base1.__init__(self)
		Base2.__init__(self)
		self.Value1 = 50
		self.Value2 = 60
		print("Inside Derived __init__ method.!")

	def sun(self):
		print("Inside Derived sun.!")

def main():
	bobj1 = Base1()		# Object of Base class

	print(bobj1.no1)
	print(bobj1.no2)
	bobj1.fun()			# Base1 fun() 
	bobj1.gun()			# Base1 gun()

	bobj2 = Base2()	# Object of Derived1 class

	print(bobj2.num1)
	print(bobj2.num2)
	bobj2.gun()			# Base2 gun()

	dobj = Derived()	# Object of Derived1 class

	print(dobj.no1)
	print(dobj.no2)
	print(dobj.num1)
	print(dobj.num2)
	print(dobj.Value1)
	print(dobj.Value2)
	dobj.fun()			# Base1 fun() bcz of 25th statement as Base1 is first derived
	dobj.gun()			# Base1 gun()
	dobj.sun()			# Derived sun()

if __name__ == "__main__":
	main()