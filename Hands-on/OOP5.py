class Demo:
	x = 10		# Class Variable
	y = 20		# Class Variable

	def __init__(self):
		print("Inside __init__ method.!")
		self.i = 30		# Instance Variable
		self.j = 40		# Instance Variable

	def __del__(self):
		print("Inside __del__ method.!")

	def fun(self):
		print("Inside fun method.!")

def main():
	obj1 = Demo()	# Demo(obj1) -> Demo(__init__())
	obj1.fun()		# fun(obj1)  -> fun(1000)

	obj2 = Demo()	# Demo(obj2) -> Demo(__init__())
	obj2.fun()		# fun(obj2)  -> fun(2000)

	del obj1
	del obj2

	# UnboundLocalError: local variable 'obj1' referenced before assignment
	# obj1.fun()

if __name__ == "__main__":
	main()