# Program to demonstrate implementation of File Handling.

def main():
	file_name = input("Enter the File name You want to Create : ")

	# Creates new file
	fobj = open(file_name,"w")
	print("File Created Successfully...!!!")

if __name__ == "__main__":
	main()