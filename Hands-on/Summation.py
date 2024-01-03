def Summation(*Numbers):
	Sum = 0
	for No in Numbers:
		Sum = Sum + No
	return Sum

def main():
	Ret = Summation(10,20)
	print("Addition is : ",Ret)

	Ret = Summation(10,20,30,40,50)
	print("Summation is : ",Ret)

if __name__ == "__main__":
	main()