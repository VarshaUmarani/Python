# Application to demonstrate creation of DataFrame using Pandas.

import pandas as pd

def main():
	df1 = {'One':pd.Series([1,2,3],index=['a','b','c']),
	'Two':pd.Series([1,2,3,4],index=['a','b','c','d'])}

	df2 = {'One':pd.Series([1,2,3],index=['a','b','c']),
	'Two':pd.Series([1,2,3,4],index=['a','b','c','d'])}

	data = {'Item1' : df1, 'Item2' : df2}

	# Panel is deprecated in Python-3
	dataframe = pd.DataFrame(data)
	print(dataframe)

if __name__ == "__main__":
	main()