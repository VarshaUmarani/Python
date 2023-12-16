# Design automation script which accept directory name and write names of duplicate files from that directory into log file.
# Log file should be created into current directory.

# Usage : DirectoryDuplicate.py “Demo”
# Demo is name of directory.

import os
import time
import hashlib
import schedule
from sys import *
from datetime import datetime

def CalculateCheckSum(path,blocksize = 1024):
	fd = open(path,"rb")
	hobj = hashlib.md5()

	buffer = fd.read(blocksize)
	while len(buffer) > 0:
		hobj.update(buffer)
		buffer = fd.read(blocksize)

	fd.close()
	return hobj.hexdigest()

def DirectoryTraversal(path):
	if not os.path.exists(path):
		print("Error : The path you entered doesn't exists.!")
		exit()

	iCnt = 0
		
	duplicate = {}		# Dictionary to hold checksum and file name

	for Folder, Subfolder, Filename in os.walk(path):
		for file in Filename:
			iCnt += 1
			actualpath = os.path.join(Folder,file)
			hash = CalculateCheckSum(actualpath)
			
			if hash in duplicate:					# If checksum is already present
				duplicate[hash].append(actualpath)
			else:
				duplicate[hash] = [actualpath]		# If checksum is not present

	return duplicate,iCnt

def Create_LogFile(path):

	folder_Name = os.getcwd()

	file_name = os.path.join(folder_Name,"%s.log" %(datetime.now().strftime("%H-%M-%S")))

	file = open(file_name,'w')

	files, file_count = DirectoryTraversal(path)
	duplicate_files = Find_Duplicate(files)

	if len(duplicate_files) != 0:
		file.write("Name of duplicate files are : \n")
		for fileName in duplicate_files:
			file.write("%s\n" %(fileName))

	file.write("Overall Statistics : \n")
	file.write("Total Number of Files Scanned is : %s\n" %(file_count))

	if len(duplicate_files) == 0:
		file.write("There are no duplicate files in the specified directory..!!\n")
	else:
		file.write("Total Number of Duplicate Files found is : %s\n" %len(duplicate_files))

	file.close()

def Find_Duplicate(duplicate):
	output = list(filter(lambda x : len(x) > 1,duplicate.values()))

	iCnt = 0
	i = 0
	Arr = []
	for result in output:
		iCnt = 0
		for path in result:
			iCnt = iCnt + 1
			if iCnt >= 2:
				i = i + 1
				Arr.append(path)

	return Arr

def main():

	print("-------------------------------  Automation Script for Directory Traversal and Display Duplicate Files in Log file  ------------------------------")

	if len(argv) != 2:
		print("Error : Insufficient Argument to the script.!")
		exit()

	if (argv[1] == "-h") or (argv[1] == "-H"):
		print("Script Help : This Script works as Directory Traversal and Display Duplicate Files.!")
		exit()

	if (argv[1] == "-u") or (argv[1] == "-U"):
		print("Script Usage : Parameters - Application_Name.py Absolute Path of the Destination Directory")
		exit()

	Create_LogFile(argv[1])
	print("The given Task completed successfully...!!!")

if __name__ == "__main__":
	main()