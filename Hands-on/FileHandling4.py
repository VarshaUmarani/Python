# Program to demonstrate implementation of File Handling.

def main():
	file_name = input("Enter the File name You want to Read : ")

	# open() method opens the file in read mode
	fobj = open(file_name,"r")

	size = int(input("Enter number of bytes to fetch from file : "))

	print(fobj.read(size))
	print("Data Read from file Successfully...!!!")

if __name__ == "__main__":
	main()