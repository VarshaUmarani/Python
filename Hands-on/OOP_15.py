class Demo:
	def __init__(self):
		self.public = 10
		self._protected = 20
		self.__private = 30

	def publicFun(self):
		print("public fun.!")

	def _protectedFun(self):
		print("protected fun.!")

	def __privateFun(self):
		print("private fun.!")

def main():
	obj = Demo()
	print(obj.public)			# 10
	print(obj._protected)		# 20
	# print(obj.__private)		# Not allowed as _private is private member
	print(obj._Demo__private)	# 30

	obj.publicFun()				# public fun
	obj._protectedFun()			# protected fun
	# obj.__privateFun()		# Not allowed as _privateFun is private method
	obj._Demo__privateFun()		# private fun

if __name__ == "__main__":
	main()