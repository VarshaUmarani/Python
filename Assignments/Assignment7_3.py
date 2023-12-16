# Write a program which contains one class named as Numbers. 
# Numbers class contains one instance variables as Value. 
# Inside init method initialise that instance variables to the value which is accepted from user. 
# There are four instance methods inside class as ChkPrime(), ChkPerfect(), SumFactors(), Factors(). 
# ChkPrime() method will returns true if number is prime otherwise return false. 
# ChkPerfect() method will returns true if number is perfect otherwise return false.
# Factors() method will display all factors of instance variable. 
# SumFactors() method will return addition of all factors. Use this method in any another method 
# as a helper method if required. 
# After designing the above class call all instance methods by creating multiple objects.

class Numbers:
	def __init__(self,No):
		self.Num = No

	def CheckPrime(self):
		Flag = 0
		for i in range(2,int(self.Num/2)+1):
			if self.Num % i == 0:
				Flag = 1
				break
		if Flag == 0:
			return True
		else:
			return False

	def CheckPerfect(self):
		Sum = 0
		for i in range(1,int(self.Num/2)+1):
			if self.Num % i == 0:
				Sum = Sum + i

		if Sum == self.Num:
			return True
		else:
			return False

	def Factors(self):
		factors = []
		for i in range(1,int(self.Num/2)+1):
			if self.Num % i == 0:
				factors.append(i)

		return factors

	def SumOfFactors(self):
		Sum = 0
		for i in range(1,int(self.Num/2)+1):
			if self.Num % i == 0:
				Sum = Sum + i

		return Sum

def main():
	No = int(input("Enter the Number : "))

	Obj = Numbers(No)
	Ret = Obj.CheckPrime()
	if Ret == True:
		print("{} is Prime Number".format(No))
	else:
		print("{} is not Prime Number.!".format(No))

	Ret = Obj.CheckPerfect()
	if Ret == True:
		print("{} is Perfect Number".format(No))
	else:
		print("{} is not Perfect Number.!".format(No))

	Fact = Obj.Factors()
	print("Factors of {} are : {}".format(No,Fact))

	Sum = Obj.SumOfFactors()
	print("Sum of Factors of {} is : {}".format(No,Sum))

if __name__ == "__main__":
	main()