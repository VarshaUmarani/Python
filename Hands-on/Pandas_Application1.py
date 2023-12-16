# Application to demonstrate the creation of Data Frames using Pandas library.
# There are multiple ways in which we can create Data Frames using Pandas.

import pandas as pd

def main():
	print("Empty data frame")
	# data frame
	df = pd.DataFrame()
	print(df)

	print("DataFrame with list")
	data = [1,2,3,4,5]
	df = pd.DataFrame(data)
	print(df)

	print("DataFrame with list")
	data = [['C',1],['C++',2],['Java',3],['Python',4]]
	df = pd.DataFrame(data,columns=['ProgrammingLanguage','Experience'])
	print(df)

	data = {'Name':['C','C++','Java','Python'],'Experience':[1,2,3,4]}
	df = pd.DataFrame(data)
	print(df)

	data = [{'ProgrammingLanguage':'C','Experience':1},
	{'ProgrammingLanguage':'C++','Experience':2},
	{'ProgrammingLanguage':'Java','Experience':3},
	{'ProgrammingLanguage':'Python','Experience':4}]
	df = pd.DataFrame(data)
	print(df)

	d = {'One':pd.Series([1,2,3], index=['a','b','c']),
	'Two':pd.Series([1,2,3,4], index=['x','y','z','w'])}
	df =pd.DataFrame(d)
	print(df['One'])
	print(df['Two'])
	print(df)

if __name__ == "__main__":
	main()