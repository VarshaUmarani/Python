# If Base class and Derived Class have method with the same name,
# then due to overriding the method inside derived class gets called,
# If we want to avoid this, there are several way in which we can call base class method.

class Base:
	def __init__(self):
		self.i = 10
		self.j = 20

	def fun(self):
		print("Base fun.!")

class Derived(Base):
	def __init__(self):
		# self.__init__(self)		# RecursionError : It will exceed recursion limit
		# super().__init__()
		Base.__init__(self)
		self.x = 30
		self.y = 40

	def fun(self):
		print("Derived gun.!")
		Base.fun(self)
		# self.fun()		# fun(self)	-> RecursionError : It will exceed recursion limit
		super().fun()	# fun(self)

		# print(i)		# AttributeError
		print(self.i)
		# print(super().i)	# AttributeError

def main():
	dobj = Derived()
	dobj.fun()

if __name__ == "__main__":
	main()