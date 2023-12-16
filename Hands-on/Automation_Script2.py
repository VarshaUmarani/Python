from sys import *

def Function(value):
	print("Inside Function with parameter : ",value)

def main():
	print("-------------------- Automation Script using Python -------------------------")

	print("Script Title : ",argv[0])

	if (len(argv) != 2):
		print("Error : Insufficient Argument to the script.!")
		exit()

	if (argv[1] == "-u") or (argv[1] == "-U"):
		print("Script Usage : Run the script as parameter followed by file name.!")
		exit()

	if (argv[1] == "-h") or (argv[1] == "-H"):
		print("This is Automation Script")
		exit()

	Function(argv[1])

if __name__ == "__main__":
	main()