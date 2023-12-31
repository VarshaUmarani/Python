# Implementation of Equal to or not and greater than operator overloading

class Student:
	def __init__(self,str,a,b,c):
		self.name = str
		self.m1 = a
		self.m2 = b
		self.m3 = c

	def __eq__(self,other):
		return (self.m1 == other.m1) and (self.m2 == other.m2) and (self.m3 == other.m3)
		
	def __gt__(self,other):
		return (self.m1 > other.m1) and (self.m2 > other.m2) and (self.m3 > other.m3)

def main():
	obj1 = Student("Varsha",98,95,83)
	obj2 = Student("Vaishali",94,91,81)

	if obj1 == obj2:
		print("Both the Students are same.!")
	else:
		print("Both the Students are different.!")

	if obj1 > obj2:
		print("First object is greater.!")
	else:
		print("Second obj is greater.!")

if __name__ == "__main__":
	main()