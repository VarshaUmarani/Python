# Design Object Oriented Programming Python application which Accept N numbers from user and perform below operations.
# list out all even numbers, odd numbers,
# prime numbers and perfect numbers separately.
# Calculate summation of all numbers.

# Input : 7
# Elements : [6, 28, 11, 17, 5, 35, 44]
# Even Numbers : [6, 28, 44]
# Odd Numbers : [11, 17, 5, 35]
# Prime Numbers : [11, 17, 5]
# Perfect Numbers : [6, 28]
# Summation : 146

class Numbers:
	# Here __init__() method works both as default constructor and parameterised constructors 
	def __init__(self,Length = 5):
		self.Size = Length
		self.List = []

	def Accept(self):
		for i in range(self.Size):
			No = int(input("Enter Element Number {} : ".format(i+1)))
			self.List.append(No)

	def Display(self):
		print("Entered Elements are : ",self.List)

	def EvenNumbers(self):
		Even_Numbers = []
		for i in range(self.Size):
			if self.List[i] % 2 == 0:
				Even_Numbers.append(self.List[i])

		return Even_Numbers

	def OddNumbers(self):
		Odd_Numbers = []
		for i in range(self.Size):
			if self.List[i] % 2 != 0:
				Odd_Numbers.append(self.List[i])

		return Odd_Numbers

	def PrimeNumbers(self):
		Flag = False
		Prime_Numbers = []
		for i in range(self.Size):
			Flag = 0
			for j in range(2,int(self.List[i]/2)+1):
				if self.List[i] % j == 0:
					Flag = True
					break
			if Flag == False:
				Prime_Numbers.append(self.List[i])

		return Prime_Numbers

	def PerfectNumbers(self):
		Sum = 0
		Perfect_Numbers = []
		for i in range(self.Size):
			for j in range(1,int(self.List[i]/2)+1):
				if self.List[i] % j == 0:
					Sum = Sum + j
			if Sum == self.List[i]:
				Perfect_Numbers.append(self.List[i])

			Sum = 0

		return Perfect_Numbers

	def Summation(self):
		Sum = 0
		for i in range(self.Size):
			Sum = Sum + self.List[i]

		return Sum

	def __del__(self):
		print("Deallocating the memory of the object.!")
		del self.List

def main():
	Size = int(input("Enter Number of Elements : "))

	obj = Numbers(Size)

	obj.Accept()
	obj.Display()

	Even_Numbers = obj.EvenNumbers()
	print("List of Even Numbers is : ",Even_Numbers)

	Odd_Numbers = obj.OddNumbers()
	print("List of Odd Numbers is : ",Odd_Numbers)

	Prime_Numbers = obj.PrimeNumbers()
	print("List of Prime Numbers is : ",Prime_Numbers)

	Perfect_Numbers = obj.PerfectNumbers()
	print("List of Perfect Numbers is : ",Perfect_Numbers)

	Sum = obj.Summation()
	print("Summation of all the Numbers in list is : ",Sum)

	del obj

if __name__ == "__main__":
	main()