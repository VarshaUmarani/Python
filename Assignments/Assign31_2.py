# Write application which accept file name from user and create that file. 

# Input : Demo.txt 
# Output : File created successfully.

def Create_File(Name):
	try:
		fobj = open(Name,"r")
		print("File Opened Successfully...!!!")
	except Exception as e:
		fobj = open(Name,"w")
		print("File Created Successfully...!!!")

def main():
	name = input("Enter File Name to Create File : ")

	Create_File(name)

if __name__ == "__main__":
	main()