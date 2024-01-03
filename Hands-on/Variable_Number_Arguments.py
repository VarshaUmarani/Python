# Variable Number of Arguments
def Summation(*Value):
	print("Number of Arguments are : ",len(Value))
	Sum = 0
	for i in Value:
		Sum = Sum + i
	return Sum

def main():
	Ret = Summation(1,2,3,4,5)
	print("Summation is : ",Ret)

	Ret = Summation(10,20,30,40,50)
	print("Summation is : ",Ret)

if __name__ == "__main__":
	main()