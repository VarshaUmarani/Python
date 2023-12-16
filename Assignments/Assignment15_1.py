# Design automation script which accept directory name and display checksum of all files.

# Usage : DirectoryChecksum.py “Demo”
# Demo is name of directory.

import os
import hashlib
from sys import *

def Calculate_CheckSum(path,blocksize = 1024):
	fd = open(path,'rb')
	hobj = hashlib.md5()

	buffer = fd.read(blocksize)
	while len(buffer) != 0:
		hobj.update(buffer)
		buffer = fd.read(blocksize)

	fd.close()
	return hobj.hexdigest()

def Directory_Traversal(path):
	iCnt = 0

	if not os.path.exists(path):
		print("Error : The path you entered doesn't exists.!")
		exit()

	print("Contents of the Directory are : ")

	for folder,subfolder,file_name in os.walk(path):
		print("Directory name is : ",folder)
		for sub in subfolder:
			print("Subfolder of",folder,"is : ",sub)
		for file in file_name:
			iCnt += 1
			print("File name is : ",file)
			actualpath = os.path.join(folder,file)
			hash = Calculate_CheckSum(actualpath)
			print(hash)

	print("Number of Total Files Scanned is :",iCnt)

def main():
	print("-------------------------- Automation Script for Directory Traversal and Checksum Calculator -------------------------")

	if len(argv) != 2:
		print("Error : Insufficient Argument to the script.!")
		exit()

	if (argv[1] == "-h") or (argv[1] == "-H"):
		print("Script Help : Automation Script for Directory Traversal and Checksum Calculator.!")
		exit()

	if (argv[1] == "-u") or (argv[1] == "-U"):
		print("Script Usage : Parameters - Application_Name.py Absolute Path of the Destination Directory")
		exit()

	Directory_Traversal(argv[1])	

if __name__ == "__main__":
	main()