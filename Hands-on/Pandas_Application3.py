# Application to demonstrate creation of Series using Pandas. 
# There are different ways in which we can create Series using Pandas.

import numpy as np
import pandas as pd

def main():
	series = pd.Series()
	print(series)

	data = np.array(['a','b','c','d'])
	series = pd.Series(data)
	print(series[0])

	data = np.array(['a','b','c','d'])
	series = pd.Series(data,index=[100,101,102,103])
	print(series[100])

	data = {'a':0.1,'b':1.1,'c':2.1}
	series = pd.Series(data)
	print(series)

	series = pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
	print(series['a'])

if __name__ == "__main__":
	main()