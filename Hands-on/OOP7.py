# Demonstration of Encapsulation 
# Definition : Binding Characteristics and behavior together.
# Characteristics : Data/attributes 
# Behavior : Method

# Types of characteristics : 1. Instance data 	 2. Class data
# Types of Behaviors :		 1. Instance method	 2. Static method 	3. Class method

# Special methods of class :
# 1. __init__() : Used to initialise the instance variables and allocate the resources
# It gets automatically called, after creating the object of class.

# 2. __del__() : Used to deallocate the resources allocated to the object
# It gets automatically called, before deallocating the memory of object.

# self keyword is compulsory to write as first parameter of method explicitly. as it
# refers to the caller object.

class Programming:
	Value = 121								# Class/Static Characteristics

	def __init__(self,No1,No2):				# Constructor
		self.Num1 = No1						# Instance Variables
		self.Num2 = No2
		print("Inside __init__ method.!")

	def Fun(self):							# Instance method
		print("Inside Fun method.!")
		print("Value of Num2 is : ",self.Num2)

	def __del__(self):						# Destructor
		print("Inside __del__ method.!")

def main():
	obj1 = Programming(11,21)				# Creating the object
	obj2 = Programming(51,101)

	print("Value of Num1 from obj1 : ",obj1.Num1)	# Accessing instance members
	print("Value of Num1 from obj2 : ",obj2.Num1)
	print("Value of Class member : ",Programming.Value)		# Accessing class member

	# Calling instance method
	obj1.Fun()							# Fun(obj1)
	obj2.Fun()							# Fun(obj2)

	del obj1					# Deallocating the memory of object
	del obj2

if __name__ == "__main__":
	main()