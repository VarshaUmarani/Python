def Addition(List):
	Sum = 0
	for i in range(len(List)):
		Sum = Sum + List[i]
	return Sum

def main():
	Arr = [10,20,30,40,50]

	Ret = Addition(Arr)
	print("Addition is : ",Ret)

if __name__ == "__main__":
	main()