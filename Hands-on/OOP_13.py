class Base1:
	def __init__(self):
		print("Inside Base1 Constructor")

	def fun(self):
		print("Base1 fun")

class Base2:
	def __init__(self):
		print("Inside Base2 Constructor")

	def fun(self):
		print("Base2 fun")

class Derived(Base1,Base2):
	def __init__(self):
		Base1.__init__(self)
		Base2.__init__(self)
		print("Inside Derived Constructor")

	def fun(self):				# Overriding
		print("Derived fun")

def main():
	dobj = Derived()
	dobj.fun()			# Derived fun

if __name__ == "__main__":
	main()