# Create one module named as Maths which contains 4 functions as Add() for addition, Sub() for subtraction, Mult() for multiplication
# and Div() for division. All functions accepts two parameters as number and perform the operation. Write on python program which call all
# the functions from Maths module by accepting the parameters from user.

from MathsModule import *

def main():
	No1 = int(input("Enter First Number : "))
	No2 = int(input("Enter Second Number : "))

	Add = Addition(No1,No2)
	Sub = Subtraction(No1,No2)
	Mult = Multiplication(No1,No2)
	Div = Division(No1,No2)

	print("Addition of {} and {} is : {}".format(No1,No2,Add))
	print("Subtraction of {} and {} is : {}".format(No1,No2,Sub))
	print("Multiplication of {} and {} is : {}".format(No1,No2,Mult))
	
	if Div == -1:
		print("Cannot divide number by 0.!")
	else:
		print("Division of {} and {} is : {}".format(No1,No2,int(Div)))

if __name__ == "__main__":
	main()