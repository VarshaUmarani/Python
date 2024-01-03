# Accept input from user and perform Addition, Subtraction, Multiplicatio, Division and Modular division.
# Using Object Oriented Programming

# Input : 11 10
# Output :
# Addition : 21
# Subtraction : 1
# Multiplication : 110
# Division : 1
# Modulas : 1

# In Object Oriented Programming terminology,
# Characteristics : What we need to perform action
# Behaviour : What is the action to perform

class Arithmetic():						# Class Definition
	Value = 111							# Class Variable

	def __init__(self,No1,No2):			# Class Constructor
		self.Num1 = No1				# Instance Variable
		self.Num2 = No2				# Instance Variable

	def Addition(self):					# Instance Method
		Add = self.Num1 + self.Num2
		return Add

	def Subtraction(self):				# Instance Method
		Sub = self.Num1 - self.Num2
		return Sub

	def Multiplication(self):			# Instance Method
		Mult = self.Num1 * self.Num2
		return Mult

	def Division(self):					# Instance Method
		if self.Num2 == 0:
			return -1
		else:
			Div = self.Num1 / self.Num2
			return Div

	def Modulus(self):					# Instance Method
		if self.Num2 == 0:
			return -1
		else:
			Mod = self.Num1 % self.Num2
			return Mod

def main():
	Value1 = int(input("Enter First Number : "))
	Value2 = int(input("Enter Second Number : "))

	obj = Arithmetic(Value1,Value2)		# __init__(obj,Value1,Value2)

	print("Value of Class Variable is : ",Arithmetic.Value)		# We can access class variable outside the class.

	Ret = obj.Addition()		# Addition(obj)
	print("Addition of {} and {} is : {}".format(Value1,Value2,Ret))

	Ret = obj.Subtraction()		# Subtraction(obj)
	print("Subtraction of {} and {} is : {}".format(Value1,Value2,Ret))

	Ret = obj.Multiplication()	# Multiplication(obj)
	print("Multiplication of {} and {} is : {}".format(Value1,Value2,Ret))

	Ret = obj.Division()		# Division(obj)
	if Ret == -1:
		print("Division by 0 is not possible.!")
	else:
		print("Division of {} and {} is : {}".format(Value1,Value2,int(Ret)))

	Ret = obj.Modulus()
	if Ret == -1:
		print("Division by 0 is not possible.!")
	else:
		print("Modulus of {} and {} is : {}".format(Value1,Value2,Ret))

if __name__ == "__main__":
	main()