# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
# Author: Varsha Sidaray Umarani
# Date :  27-October-2023
# About:  Automation Script to Display the Username, Name and ID of the running processes.
#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

import psutil
from sys import *

def Display_Process():
	Data = []

	for process in psutil.process_iter():
		value = process.as_dict(attrs = ['pid','name','username'])
		Data.append(value)

	return Data

def main():
	print("--------------- Automation Script to Display Information of Running Processes ---------------")

	print("Script Title : ",argv[0])

	process = Display_Process()

	print("List of Running Processes")
	
	for element in process:
		print(element)

if __name__ == "__main__":
	main()