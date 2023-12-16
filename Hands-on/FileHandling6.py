# Program to demonstrate implementation of File Handling.
# Program to read content of file using for loop.

def main():
	file_name = input("Enter the File name You want to Read : ")

	# open() method opens the file in read mode
	fobj = open(file_name,"r")

	print("Data from file is : ")

	# Here, Loop will traverse line by line, and data will be displayed line by line.
	for data in fobj:
		# print(data)	# Here, new line will be added after each and every line of data.
		# To avoid this, we can write
		print(data,end="")
		
	print()
	print("Data Read from file Successfully...!!!")

if __name__ == "__main__":
	main()