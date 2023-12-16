# Write application which accept file name from user and display size of file. 

# Input : Demo.txt 
# Output : File size is 56 bytes

def Size_File(Name):
	Cnt = 0
	try:
		fobj = open(Name,"r")
		str = fobj.read()
		for s in str:
			Cnt = Cnt + 1
	except Exception as e:
		print("No File Named %s"%(Name))
		return
	finally:
		fobj.close()
		return Cnt

def main():
	name = input("Enter File Name : ")

	Ret = Size_File(name)
	print("Size of the File is :",Ret)

if __name__ == "__main__":
	main()