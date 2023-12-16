# Write a program which contains one class named as Demo. 
# Demo class contains two instance variables as no1 ,no2. 
# That class contains one class variable as Value. 
# There are two instance methods of class as Fun and Gun which displays values of instance variables. 
# Initialise instance variable in init method by accepting the values from user. 
 
# After creating the class create the two objects of Demo class as 
# Obj1 = Demo(11,21) 
# Obj2 = Demo(51,101) 
# Now call the instance methods as 
# Obj1.Fun() 
# Obj2.Fun() 
# Obj1.Gun() 
# Obj2.Gun()

class Demo:
	Value = 0			# Class Variable

	def __init__(self,Num1,Num2):
		self.No1 = Num1				# Instance Variables
		self.No2 = Num2

	def Fun(self):					# Instance Methods
		print(self.No1)

	def Gun(self):
		print(self.No2)

def main():
	Value1 = int(input("Enter First Number : "))
	Value2 = int(input("Enter Second Number : "))

	obj1 = Demo(Value1,Value2)
	obj1.Fun()
	obj1.Gun()

	Value1 = int(input("Enter First Number : "))
	Value2 = int(input("Enter Second Number : "))

	obj2 = Demo(Value1,Value2)
	obj2.Fun()
	obj2.Gun()

if __name__ == "__main__":
	main()