# Write a program which contains one class named as Arithmetic.
# Arithmetic class contains two instance variables as Value1 ,Value2.
# Inside init method initialise all instance variables to 0.
# There are instance methods inside class as Accept(), Addition(), Subtraction(),
# Multiplication(), Division() and Modulus().
# Accept method will accept value of Value1 and Value2 from user.
# Addition() method will perform addition of Value1 ,Value2 and return result.
# Subtraction() method will perform subtraction of Value1 ,Value2 and return result.
# Multiplication() method will perform multiplication of Value1 ,Value2 and return result.
# Division() method will perform division of Value1 ,Value2 and return result.
# Modulus() method will perform Modulus of Value1 ,Value2 and return result.
# After designing the above class call all instance methods by creating multiple objects.

class Arithmetic:
	def __init__(self):
		self.Value1 = 0
		self.Value2 = 0

	def Accept(self):
		self.Value1 = int(input("Enter First Number : "))
		self.Value2 = int(input("Enter Second Number : "))

	def Addition(self):
		return self.Value1 + self.Value2

	def Subtraction(self):
		return self.Value1 - self.Value2

	def Multiplication(self):
		return self.Value1 * self.Value2

	def Division(self):
		if self.Value2 == 0:
			return -1
		else:
			return int(self.Value1 / self.Value2)

	def Modulus(self):
		if self.Value2 == 0:
			return -1
		else:
			return self.Value1 % self.Value2

def main():
	Obj = Arithmetic()
	Obj.Accept()

	Add = Obj.Addition()
	print("Addition is : ",Add)

	Sub = Obj.Subtraction()
	print("Subtraction is : ",Sub)

	Mult = Obj.Addition()
	print("Addition is : ",Mult)

	Div = Obj.Division()
	if Div == -1:
		print("Division by 0 is not possible.!")
	else:
		print("Division is : ",Div)

	Mod = Obj.Modulus()
	if Mod == -1:
		print("Division by 0 is not possible.!")
	else:
		print("Modulus is : ",Mod)

if __name__ == "__main__":
	main()