# Accept two Numbers from user and perform Addition of that numbers

# import ArithmeticModule
# from ArithmeticModule import Addition, Subtraction
# from ArithmeticModule import *

import ArithmeticModule as AM

# Entry Point Function
def main():
	#print("__name__ from main is : ",__name__)		# __main__
	No1 = int(input("Enter First Number : "))
	No2 = int(input("Enter Second Number : "))

	Ret = AM.Addition(No1,No2)
	print("Addition of {} and {} is : {}".format(No1,No2,Ret))

	Ret = AM.Subtraction(No1,No2)
	print("Subtraction of {} and {} is : {}".format(No1,No2,Ret))

# Code Starter
if __name__ == "__main__":
	main()