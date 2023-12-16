# Application to demonstrate operations on Excel file using Pandas Library.

import pandas as pd

def main():
	# dataset = pd.read_excel("Pandas.xlsx",sheet_name=0)
	dataset = pd.read_excel("Pandas.xlsx",sheet_name="Sheet")

	# 1 way to read columns from sheet
	Names = dataset["ProgrammingLanguage"].values
	Experience = dataset["Experience"].values

	print(Names)
	print(Experience)

	# 2 way to read columns from sheet
	Names = dataset.ProgrammingLanguage
	Experience = dataset.Experience

	print(Names)
	print(Experience)

if __name__ == "__main__":
	main()