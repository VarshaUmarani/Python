# Demonstration of Polymorphism
# In Python, method overloading is not possible, but we can achieve the feel of method overloading.

class Arithmetic:
	def Add(self,no1=None,no2=None,no3=None):
		if no1 != None and no2 != None and no3 != None:
			return no1 + no2 + no3
		elif no1 != None and no2 != None:
			return no1 + no2
		elif no1 != None:
			return no1
		else:
			return 0

	# def Add(self,no1,no2,no3):
	#	return no1 + no2 + no3

	# This method overlaps the method defined on line 15.
	# def Add(self,no1,no2):
	#	return no1 + no2

def main():
	obj = Arithmetic()

	print(obj.Add(10,20,30))
	print(obj.Add(10,20))
	print(obj.Add(10))
	print(obj.Add())

if __name__ == "__main__":
	main()