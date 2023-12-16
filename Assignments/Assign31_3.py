# Write application which accept file name from user and read all data from that file and display contents on screen. 

# Input : Demo.txt 
# Output : Display all data of file.

def Read_File(Name):
	try:
		fobj = open(Name,"r")
		str = fobj.read()
		print(str)
	except Exception as e:
		print("No File Named %s"%(Name))
		return

def main():
	name = input("Enter File Name : ")

	Read_File(name)

if __name__ == "__main__":
	main()