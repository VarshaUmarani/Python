def Display(Num,Msg = "Jay Ganesh...!!!"):
	iCnt = 0

	if Num < 0:
		Num = -(Num)

	while iCnt < Num:
		print(Msg)
		iCnt = iCnt + 1

def main():
	print("Enter Number of Iterations : ")
	Value = int(input())

	print("Enter the Message : ")
	Message = input()

	Display(Value,Message)
	
	Display(Value)

if __name__ == "__main__":
	main()