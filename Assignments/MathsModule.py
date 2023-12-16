# All the functions accept two parameters as Num1, Num2 and perform the Operation and return the result.

# Definition of Addition Function
def Addition(Num1,Num2):
	Add = Num1 + Num2
	return Add

# Definition of Subtraction Function
def Subtraction(Num1,Num2):
	Sub = Num1 - Num2
	return Sub

# Definition of Multilication Function
def Multiplication(Num1,Num2):
	Mult = Num1 * Num2
	return Mult

# Definition of Division Function
def Division(Num1,Num2):
	if Num2 == 0:
		return -1
	else:
		Div = Num1 / Num2
		return Div