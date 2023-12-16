# Write application which accept file name from user and open that file in read mode. 

# Input : Demo.txt 
# Output : File opened successfully.

def Open_File(Name):
	
	try:
		fobj = open(Name,"r")
	except Exception as e:
		print("No File Named :",Name)
		return
	else:
		print("File Opened Successfully...!!!")

def main():
	Name = input("Enter File Name : ")

	Open_File(Name)

if __name__ == "__main__":
	main()