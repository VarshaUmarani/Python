# Application to demonstrate creating DataFrame using Pandas and writhe the contents of that
# DataFrame in xlsx file using ExcelWriter.

import pandas as pd

def main():
	data = [{'ProgrammingLanguage':'C','Experience':1},
	{'ProgrammingLanguage':'C++','Experience':2},
	{'ProgrammingLanguage':'Java','Experience':3},
	{'ProgrammingLanguage':'Python','Experience':4}]

	df = pd.DataFrame(data)
	print(df)

	writer = pd.ExcelWriter("Pandas.xlsx",engine='xlsxwriter')

	df.to_excel(writer,sheet_name='Sheet')

	writer._save()

if __name__ == "__main__":
	main()