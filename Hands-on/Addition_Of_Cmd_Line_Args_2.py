import sys

def Addition(No1,No2):
	Ans = No1 + No2
	return Ans

def main():
	if len(sys.argv) < 3 or len(sys.argv) > 3:
		print("Invalid Number of arguments...!!!")
		return

	Ret = Addition(int(sys.argv[1]),int(sys.argv[2]))
	print("Addition of {0} and {1} is : {2}".format(sys.argv[1],sys.argv[2],Ret))

if __name__ == "__main__":
	main()