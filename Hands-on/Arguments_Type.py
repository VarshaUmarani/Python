# Positional arguments
def StudentData(Name,RollNo,Address,Marks):
	print("Name is : ",Name)
	print("Roll Number is : ",RollNo)
	print("Address is : ",Address)
	print("Marks obtained : ",Marks)

# Keyword Arguments
def ComputerData(RAM,Processor,SSD):
	print("RAM Size is : ",RAM)
	print("Processor is : ",Processor)
	print("Size of SSD is : ",SSD)

# default arguments
# default argument order should be from right to left
def AreaofCircle(Radius,PI=3.14):
	print("Value of PI is : ",PI)
	Area = PI * (Radius **2)
	return Area

# Variable Number of Arguments
def Summation(*Value):
	print("Number of Arguments are : ",len(Value))
	Sum = 0
	for i in Value:
		Sum = Sum + i
	return Sum

def main():
	# Positional arguments
	StudentData("Varsha Umarani",38,"Sangli",95)

	# Keyword Arguments
	ComputerData(RAM=16,SSD="512 GB",Processor="i5")
	ComputerData(Processor="i7",RAM=8,SSD="256 GB")

	# default arguments
	AreaofCircle(10)
	AreaofCircle(10.25,3.15)

	# Variable Number of Arguments
	Ret = Summation(1,2,3,4,5)
	print("Summation is : ",Ret)

if __name__ == "__main__":
	main()