# Duck typing in python :

class C:
	def LearnandCode(self):
		print("Learning C Programming.!")

class CPP:
	def LearnandCode(self):
		print("Learning C++ Programming.!")

class Python:
	def LearnandCode(self):
		print("Learning Python Programming.!")

class Demo:
	pass

class Programmer:
	def Coding(self,language):
		language.LearnandCode()

def main():
	cobj = C()
	cppobj = CPP()
	pobj = Python()
	dobj = Demo()

	obj = Programmer()
	obj.Coding(cobj)
	obj.Coding(cppobj)
	obj.Coding(pobj)

	# AttributeError: 'Demo' object has no attribute 'LearnandCode'
	# obj.Coding(dobj)

if __name__ == "__main__":
	main()