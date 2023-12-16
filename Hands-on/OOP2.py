# Accept input from user and perform Addition, Subtraction, Multiplicatio, Division and Modular division.
# Using Procedural Programming

# Input : 11 10
# Output :
# Addition : 21
# Subtraction : 1
# Multiplication : 110
# Division : 1
# Modulas : 1

def Addition(No1,No2):
	Add = No1 + No2
	return Add

def Subtraction(No1,No2):
	Sub = No1 - No2
	return Sub

def Multiplication(No1,No2):
	Mult = No1 * No2
	return Mult

def Division(No1,No2):
	if No2 == 0:
		return -1
	else:
		Div = No1 / No2
		return Div

def Modulus(No1,No2):
	if No2 == 0:
		return -1
	else:
		Mod = No1 % No2
		return Mod

def main():
	Value1 = int(input("Enter First Number : "))
	Value2 = int(input("Enter Second Number : "))

	Ret = Addition(Value1,Value2)
	print("Addition of {} and {} is : {}".format(Value1,Value2,Ret))

	Ret = Subtraction(Value1,Value2)
	print("Subtraction of {} and {} is : {}".format(Value1,Value2,Ret))

	Ret = Multiplication(Value1,Value2)
	print("Multiplication of {} and {} is : {}".format(Value1,Value2,Ret))

	Ret = Division(Value1,Value2)
	if Ret == -1:
		print("Division by 0 is not possible.!")
	else:
		print("Division of {} and {} is : {}".format(Value1,Value2,int(Ret)))

	Ret = Modulus(Value1,Value2)
	if Ret == -1:
		print("Division by 0 is not possible.!")
	else:
		print("Modulus of {} and {} is : {}".format(Value1,Value2,Ret))

if __name__ == "__main__":
	main()