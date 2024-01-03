# Program to demonstrate implementation of File Handling.
# Program to copy the data from one file to another.

def main():
	file_name1 = input("Enter the File name : ")

	# open() method opens the file in read mode
	fobj1 = open(file_name1,"r")
	data = fobj1.read()

	file_name2 = input("Enter the file name to copy the content : ")

	# here, open() method will create the file if it is not present. else it will open the file in write mode.
	fobj2 = open(file_name2,"w")
	
	fobj2.write(data)

	print("Data Copied Successfully..!!!")

if __name__ == "__main__":
	main()