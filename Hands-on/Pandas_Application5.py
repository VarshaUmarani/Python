# Application to demonstrate operations on Excel file using Pandas Library.

import pandas as pd

def main():
	excel_file = 'StudentInfo.xlsx'
	batches = pd.read_excel(excel_file)

	# It will display first five records of data frame
	print(batches.head())

	batches_sheet1 = pd.read_excel(excel_file,sheet_name=0,index_col=0)
	print(batches_sheet1.head())

	xlsx = pd.ExcelFile(excel_file)
	batches_sheets = []

	for sheet in xlsx.sheet_names:
		print(sheet)
		batches_sheets.append(xlsx.parse(sheet))

	batches = pd.concat(batches_sheets)
	print(batches)

if __name__ == "__main__":
	main()