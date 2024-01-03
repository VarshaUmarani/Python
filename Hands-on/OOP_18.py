# Accessing Base class variable using Base() object

class Base:
	def __init__(self):
		self.i = 10

	def fun(self):
		print("Base fun.!")

class Derived(Base):
	def __init__(self):
		Base.__init__(self)
		self.i = 30
		self.j = 40

	def gun(self):
		print("Derived gun.!")
		print(self.i)			# 30
		# Base() is used for only characteristics
		print(Base().i)			# 10

def main():
	dobj = Derived()
	dobj.gun()

if __name__ == "__main__":
	main()