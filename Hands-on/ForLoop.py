def Display(Value):
	if Num < 0:
		Num = -(Num)
		
	print("Output of For loop")
	for i in range(Value):
		print("Jay Ganesh...!!!")

def main():
	No = int(input("Enter Number of Iterations : "))

	Display(No)

if __name__ == "__main__":
	main()
