def Fibonacci(No):
	Cnt = 0
	No1, No2 = 0,1

	while Cnt != No:
		print(No2,end = "  ")
		No1,No2 = No2,No1+No2
		Cnt += 1

def main():
	print("Enter Number of terms : ")
	No = int(input())

	Fibonacci(No)

if __name__ == "__main__":
	main()