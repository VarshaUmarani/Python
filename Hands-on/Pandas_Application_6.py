# Application to demonstrate operations on Excel file using xlsxwriter.

import os
import  fnmatch
from sys import *
import xlsxwriter

def CreateExcel(name):
	workbook = xlsxwriter.Workbook(name)

	worksheet = workbook.add_worksheet()

	worksheet.write('A1','Name')
	worksheet.write('B1','College')
	worksheet.write('C1','Mail ID')
	worksheet.write('D1','Mobile')

	workbook.close()

def main():
	print("Application name : ",argv[0])

	if (len(argv) != 2):
		print("Error : Invalid number of arguments")
		exit()

	if (argv[1] == "-h") or (argv[1] == "-H"):
		print("This Application is used to create excel file and write data into it.!")
		exit()

	if (argv[1] == "-u") or (argv[1] == "-U"):	
		print("Usage : ApplicationName - ",argv[0])
		exit()

	try:
		CreateExcel(argv[1])
	except Exception:
		print("Error : Invalid input")

if __name__ == "__main__":
	main()