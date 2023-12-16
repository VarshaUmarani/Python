# Program to demonstrate implementation of File Handling.

def main():
	file_name = input("Enter the File Name You want to Read: ")

	# open() method opens the file in read mode
	fobj = open(file_name,"r")		# r - read

	print("Content of file is : ",fobj.read())
	print("Data Read from file Successfully...!!!")

if __name__ == "__main__":
	main()