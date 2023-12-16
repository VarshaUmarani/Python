# Program to demonstrate implementation of File Handling.
# Program to read single line from file.

def main():
	file_name = input("Enter the File name You want to Read : ")

	# open() method opens the file in read mode
	fobj = open(file_name,"r")

	print("First line from file is : ",fobj.readline())
	print("Data Read from file Successfully...!!!")

if __name__ == "__main__":
	main()