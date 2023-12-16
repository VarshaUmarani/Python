# super() method and Base()

class Base:
	def __init__(self):
		self.i = 10

	def fun(self):
		print("Base fun.!")

class Derived(Base):
	def __init__(self):
		Base.__init__(self)
		self.i = 20

	def fun(self):
		print("Derived fun.!")

	def gun(self):
		print("Derived gun.!")

		self.fun()
		# super() is used to access methods of Base class 
		super().fun()

		# Base() is used to access only characteristics of Base Class
		print(Base().i)			# 10
		print(self.i)			# 20

def main():
	dobj = Derived()
	dobj.gun()

if __name__ == "__main__":
	main()