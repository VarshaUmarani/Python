# Write a program which accept file name from user and create new file named as Demo.txt and copy all contents from 
# existing file into new file. Accept file name through command line arguments. 
# Input : ABC.txt 
# Create new file as Demo.txt and copy contents of ABC.txt in Demo.txt

import sys

def main():
	if (len(sys.argv) < 0) and (len(sys.argv) > 3):
		print("Invalid Number of Arguments...!!!")

	if sys.argv[1] == sys.argv[2]:
		print("Both the file names are same.!")

	fobj1 = open(sys.argv[1],"r")
	content = fobj1.read()

	fobj2 = open(sys.argv[2],"w")
	fobj2.write(content)

	print("Content of file copied successfully..!!")

if __name__ == "__main__":
	main()
