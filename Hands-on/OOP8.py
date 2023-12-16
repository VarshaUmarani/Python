class Student:
	SchoolName = "GnyanGangotri"	 	# Class Variable

	def __init__(self,No1,No2,No3):
		self.marks1 = No1				# Instance Variable
		self.marks2 = No2
		self.marks3 = No3

	def Instance_TotalMarks(self):		# Instance method
		print("Inside Instance Method.!")
		return self.marks1 + self.marks2 + self.marks3

	@classmethod						# Decorator
	def Class_DisplaySchool(cls):		# Class method
		print("School Name is : ",cls.SchoolName)

	@staticmethod						# Decorator
	def Static_Info():					# Static method
		print("This method contains the information of School.!")

def main():
	Student.Class_DisplaySchool()		# Calling class method

	obj1 = Student(95,97,95)			# Object creation
	obj2 = Student(90,92,93)

	ret = obj1.Instance_TotalMarks()	# Calling instance method
	print("Total obtained marks : ",ret)

	Student.Static_Info()				# Calling static method

# Code starter
if __name__ == "__main__":
	main()