# Design automation script which accept directory name and two file extensions from user.
# Rename all files with first file extension with the second file extension.

# Usage : DirectoryRename.py “Demo” “.txt” “.doc”

# Demo is name of directory and .txt is the extension that we want to search and rename with .doc.
# After execution this script each .txt file gets renamed as .doc.

import os
from sys import *

def Rename_Files(path,old_extension,new_extension):
	iCnt = 0
	file_count = 0

	if not os.path.exists(path):
		print("Error : The path you entered doesn't exists.!")
		exit()

	for folder, subfolder, filename in os.walk(path):
		for file in filename:
			iCnt += 1
			actualpath = os.path.join(folder,file)
			if old_extension in os.path.splitext(actualpath):
				file_count += 1
				new_path = actualpath.replace(old_extension,new_extension)
				os.rename(actualpath,new_path)

	print("Total Number of scanned files : ",iCnt)

	if file_count != 0:
		print("Total Number of files renamed from extension {} to extension {} : {}".format(old_extension,new_extension,file_count))
	else:
		print("There are no files present in specified Directory with specified extension {}".format(old_extension))

def main():
	print("----------------------  Script to Traverse Directory and Rename files of specified extension  ----------------------")

	if len(argv) != 4:
		print("Error : Invalid Number of Arguments to Script.!!")
		exit()

	if (argv[1] == "-h") or (argv[1] == "-H"):
		print("Script Help : This Script works as Directory Traversal and Rename Files of specified extension.!")
		exit()

	if (argv[1] == "-u") or (argv[1] == "-U"):
		print("Script Usage : Parameters - Application_Name.py Absolute Path of the Destination Directory Existing Extension of file New extension of file")
		exit()

	Rename_Files(argv[1],argv[2],argv[3])

if __name__ == "__main__":
	main()