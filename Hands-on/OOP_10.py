# Demonstration of Inheritance
# Multi - level inheritance

class Base:
	def __init__(self):
		self.no1 = 10
		self.no2 = 20
		print("Inside Base __init__ method.!")

	def fun(self):
		print("Inside Base fun.!")

	def gun(self):
		print("Inside Base gun.!")

class Derived1(Base):
	def __init__(self):
		Base.__init__(self)
		self.num1 = 30
		self.num2 = 40
		print("Inside Derived1 __init__ method.!")

	def gun(self):						# Overriding
		print("Inside Derived1 gun.!")

class Derived2(Derived1):			# Multi - level inheritance
	def __init__(self):
		Derived1.__init__(self)
		self.Value1 = 50
		self.Value2 = 60
		print("Inside Derived2 __init__ method.!")

	def sun(self):
		print("Inside Derived2 sun.!")

def main():
	bobj = Base()		# Object of Base class

	print(bobj.no1)
	print(bobj.no2)
	bobj.fun()			# Base fun()
	bobj.gun()			# Base gun()

	dobj1 = Derived1()	# Object of Derived1 class

	print(dobj1.no1)
	print(dobj1.no2)
	print(dobj1.num1)
	print(dobj1.num2)
	dobj1.fun()			# Base fun()
	dobj1.gun()			# Derived1 gun()

	dobj2 = Derived2()	# Object of Derived1 class

	print(dobj2.no1)
	print(dobj2.no2)
	print(dobj2.num1)
	print(dobj2.num2)
	print(dobj2.Value1)
	print(dobj2.Value2)
	dobj2.fun()			# Base fun()
	dobj2.gun()			# Derived1 gun()
	dobj2.sun()			# Derived2 sun()

if __name__ == "__main__":
	main()