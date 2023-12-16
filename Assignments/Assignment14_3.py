# Design automation script which accept two directory names. Copy all files from first directory into second directory.
# Second directory should be created at run time.

# Usage : DirectoryCopy.py “Demo” “Temp”

# Demo is name of directory which is existing and contains files in it.
# We have to create new Directory as Temp and copy all files from Demo to Temp.

import os
import shutil
from sys import *

def Copy_Files(source_path,destination_path):
	iCnt = 0
	flag = 0
	file_count = 0

	if not os.path.exists(source_path):
		print("Error : The path you entered doesn't exists.!")
		exit()

	destination_path = os.path.abspath(destination_path)

	if not os.path.exists(destination_path):
		os.mkdir(destination_path)

	for folder, subfolder, filename in os.walk(source_path):
		for file in filename:
			iCnt += 1
			actualpath = os.path.join(folder,file)
			new_path = os.path.join(destination_path,file)		

			if os.path.exists(destination_path):
				if not os.path.exists(new_path):
					file_count += 1
					shutil.copy(actualpath,destination_path)
				else:
					flag += 1

	print("Total Number of scanned files : ",iCnt)
	
	if file_count != 0:
		print("Total Number of files copied to {} : {}".format(destination_path,file_count))
	elif flag != 0:
		print("Total Number of files already present in specified Directory : ",flag)
	else:
		print("There are no files present in Specified Source Directory")

def main():
	print("----------------------  Script to Traverse Directory and Copy files from one folder to another  ----------------------")

	if len(argv) != 3:
		print("Error : Invalid Number of Arguments to Script.!!")
		exit()

	if (argv[1] == "-h") or (argv[1] == "-H"):
		print("Script Help : This Script works as Directory Traversal and Copy files from one folder to another.!")
		exit()

	if (argv[1] == "-u") or (argv[1] == "-U"):
		print("Script Usage : Parameters - Application_Name.py Absolute Path of the Source Directory, Absolute Path of Destination Directory")
		exit()

	Copy_Files(argv[1],argv[2])

if __name__ == "__main__":
	main()