# Program to demonstrate implementation of File Handling.
# Program to replace the data of the file.

def main():
	file_name = input("Enter File Name : ")

	fobj = open(file_name,"r")		# r - read 
	data = fobj.read()
	
	fobj = open(file_name,"w")		# w - write
	data1 = data.replace("Varsha","Vaishali")
	fobj.write(data1)
	
	print("Data replaced successfully..!!!")

if __name__ == "__main__":
	main()