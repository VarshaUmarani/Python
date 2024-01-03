# Program to demonstrate implementation of File Handling.

def main():
	file_name = input("Enter the File name You want to Create : ")

	# open() method Creates new file if file is not present in "w" mode
	# If file is already present, it will open the file to perform operations
	
	fobj = open(file_name,"w")		# w - write

	str = input("Enter the data that you want to write in file : ")
	fobj.write(str)

	print("Data written into file Successfully...!!!")

if __name__ == "__main__":
	main()