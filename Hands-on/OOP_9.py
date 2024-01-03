# Demonstration of Inheritance
# Single - level inheritance

class Base:
	def __init__(self):
		self.no1 = 10
		self.no2 = 20
		print("Inside Base __init__ method.!")

	def fun(self):
		print("Inside Base fun.!")

	def gun(self):
		print("Inside Base gun.!")

# class Derived : Base			-> C++
# class Derived extends Base 	-> Java

class Derived(Base):			# Single - level inheritance
	def __init__(self):
		Base.__init__(self)
		self.num1 = 30
		self.num2 = 40
		print("Inside Derived __init__ method.!")

	def sun(self):
		print("Inside Derived sun.!")

	def gun(self):						# Overriding
		print("Inside Derived gun.!")

def main():
	bobj = Base()		# Object of Base class

	print(bobj.no1)
	print(bobj.no2)
	bobj.fun()
	bobj.gun()

	dobj = Derived()	# Object of Derived class

	print(dobj.no1)
	print(dobj.no2)
	print(dobj.num1)
	print(dobj.num2)

	dobj.fun()
	dobj.sun()
	dobj.gun()		# It will call the derived gun method 
	# Bcz, Base class method gets abstrated by Derived class method
	
if __name__ == "__main__":
	main()