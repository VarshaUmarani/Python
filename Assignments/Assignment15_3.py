# Design automation script which accept directory name and delete all duplicate files from that directory.
# Write names of duplicate files from that directory into log file.
# Log file should be created into current directory.

# Usage : DirectoryDusplicateRemoval.py “Demo”
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
		
	duplicate = {}		# Dictionary to hold checksum and file name
	iCnt = 0

	for Folder, Subfolder, Filename in os.walk(path):
		for file in Filename:
			iCnt += 1
			actualpath = os.path.join(Folder,file)
			hash = CalculateCheckSum(actualpath)
			
			if hash in duplicate:					# If checksum is already present
				duplicate[hash].append(actualpath)
			else:
				duplicate[hash] = [actualpath]		# If checksum is not present

	return iCnt,duplicate

def Create_LogFile(path,FolderName="Python"):

	folder_Name = os.getcwd()

	file_name = os.path.join(folder_Name,"%s.log" %(datetime.now().strftime("%H-%M-%S")))

	file = open(file_name,'w')

	file_count,files = DirectoryTraversal(path)
	duplicate_files = FindDuplicate(files)
	deleted_files = DeleteDuplicate(duplicate_files)

	if len(deleted_files) != 0:
		file.write("Name of deleted files are : \n")
		for fileName in deleted_files:
			file.write("%s\n" %(fileName))

	file.write("Overall Statistics : \n")
	file.write("Total Number of Files Scanned is : %s\n" %(file_count))
	file.write("Total Number of Duplicate Files found is : %s\n" %len(duplicate_files))

	if len(deleted_files) == 0:
		file.write("There are no duplicate files in the specified directory..!!\n")
	else:
		file.write("Total Number of Files deleted is : %s\n" %len(deleted_files))

	file.close()

def FindDuplicate(duplicate):
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

def DeleteDuplicate(Arr):
	deleted_files = []
	for i in range(len(Arr)):
		os.remove(Arr[i])
		deleted_files.append(Arr[i])

	return deleted_files

def main():
	Arr = {}

	print("-------------------------------  Automation Script for Directory Traversal and Delete Duplicate Files  ------------------------------")

	if len(argv) != 2:
		print("Error : Insufficient Argument to the script.!")
		exit()

	if (argv[1] == "-h") or (argv[1] == "-H"):
		print("Script Help : This Script works as Directory Traversal and Delete Duplicate Files.!")
		exit()

	if (argv[1] == "-u") or (argv[1] == "-U"):
		print("Script Usage : Parameters - Application_Name.py Absolute Path of the Destination Directory")
		exit()

	Create_LogFile(argv[1])
	print("All the Duplicate files from specified directory deleted successfully..!!!")

if __name__ == "__main__":
	main()