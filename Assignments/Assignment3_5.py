# Write a program which accept N numbers from user and store it into List. Return addition of all prime numbers from that List.
# Main python file accepts N numbers from user and pass each number to ChkPrime() function which is part of our user defined module named as 
# MarvellousNum. Name of the function from main python file should be AdditionPrime().

# Input : Number of elements : 11 
# Input Elements : 13 5 45 7 4 56 10 34 2 5 8 
# Output : 32 (13 + 5 + 7 +2 + 5)

from CheckPrimeModule import *

def AdditionPrime(List):
	Sum = 0

	for i in range(len(List)):
		if CheckPrime(List[i]):
			Sum = Sum + List[i]

	return Sum

def main():
	Arr = []

	Size = int(input("Enter Number of Elements : "))

	for i in range(Size):
		No = int(input("Enter Element at {} : ".format(i+1)))
		Arr.append(No)

	print("Entered Elements are : ",Arr)

	Ret = AdditionPrime(Arr)
	print("Addition of Prime Numbers from list is : ",Ret)

if __name__ == "__main__":
	main()