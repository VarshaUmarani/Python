# Write a program which accept two file names from user and compare contents of both the files. 
# If both the files contains same contents then display success otherwise display failure. 
# Accept names of both the files from command line. 
# Input : Demo.txt Hello.txt 
# Compare contents of Demo.txt and Hello.txt

import sys

def main():
	if (len(sys.argv) < 0) and (len(sys.argv) > 3):
		print("Invalid Number of Arguments")

	if sys.argv[1] == sys.argv[2]:
		print("Both the file names are same.!")

	fobj1 = open(sys.argv[1],"r")
	fobj2 = open(sys.argv[2],"r")

	str1 = fobj1.read()
	str2 = fobj2.read()

	if str1 == str2:
		print("Contents of Both the files are Same...!!!")
	else:
		print("Contents of Both the files are Different...!!!")

if __name__ == "__main__":
	main()