# Write a program which accepts file name from user and check whether that file exists in current directory or not. 
# Input : Demo.txt 
# Check whether Demo.txt exists or not.

def main():
	file_name = input("Enter File Name : ")

	try:
		fobj = open(file_name,"r")
		print("File exists in Current Dictionary.!")
	except Exception as obj:
		print("File Doesn't exist in Current Dictionary..!")
	finally:
		pass

if __name__ == "__main__":
	main()