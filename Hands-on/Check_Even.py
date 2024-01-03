# import NumbersModule
# import NumbersModule as NM
# from NumbersModule import *
from NumbersModule import CheckEven

def main():
	No = int(input("Enter Number : "))

	Ret = CheckEven(No)

	if Ret == True:
		print("{} is Even Number".format(No))
	else:
		print("{} is Odd Number".format(No))

if __name__ == "__main__":
	main()