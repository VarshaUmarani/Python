# If we want to access method of Base class inside Derived class, 
# We can achive this by using super() method.

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

	def gun(self):
		print("Derived gun.!")
		Base.fun(self)
		self.fun()		# fun(self)
		super().fun()	# fun(self)

		# print(i)		# AttributeError
		print(self.i)
		#print(super().i)	# AttributeError

def main():
	dobj = Derived()
	dobj.gun()

if __name__ == "__main__":
	main()