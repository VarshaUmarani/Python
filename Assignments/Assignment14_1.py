# Design automation script which accept directory name and file extension from user. Display all files with that extension.
# Usage : DirectoryFileSearch.py “Demo” “.txt”
# Demo is name of directory and .txt is the extension that we want to search.

import os
from sys import *

def Display_Files(path,extension):
	iCnt = 0
	file_count = 0
	if not os.path.exists(path):
		print("Error : The path you entered doesn't exists.!")
		exit()

	for folder, subfolder, filename in os.walk(path):
		for file in filename:
			iCnt += 1
			actualpath = os.path.join(folder,file)
			if extension in os.path.splitext(actualpath):
				print(actualpath)
				file_count += 1
			
	print("Total Number of scanned files : ",iCnt)

	if file_count != 0:
		print("Total Number of files with extension {} : {}".format(extension,file_count))
	else:
		print("There are no files present in specified Directory with specified extension {}".format(extension))

def main():
	print("----------------------  Script to Traverse Directory and Display files of specified extension  ----------------------")

	if len(argv) != 3:
		print("Error : Invalid Number of Arguments to Script.!!")
		exit()

	if (argv[1] == "-h") or (argv[1] == "-H"):
		print("Script Help : This Script works as Directory Traversal and Display Files of specified extension.!")
		exit()

	if (argv[1] == "-u") or (argv[1] == "-U"):
		print("Script Usage : Parameters - Application_Name.py Absolute Path of the Destination Directory Extension of file")
		exit()

	Display_Files(argv[1],argv[2])

if __name__ == "__main__":
	main()