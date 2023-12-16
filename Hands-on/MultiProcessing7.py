# Implementation of multi Processing
# Comparison between Serial Processing and Parallel Processing.

import os
import time
import multiprocessing

def Square(no):
	return no ** 2

def ParallelProcessing():
	start = time.time()
	arr = range(101)

	pobj = multiprocessing.Pool()

	ret = pobj.map(Square,arr)
	print("Result of Parallel Processing is : ",ret)

	end = time.time()
	print("Time required for Parallel execution : ",end-start)

def SerialProcessing():
	start = time.time()
	arr = range(101)
	ret = []

	for i in arr:
		ret.append(Square(i))

	print("Result of Serial Processing is : ",ret)
	end = time.time()
	print("Time required for Serial execution : ",end-start)

def main():
	ParallelProcessing()
	SerialProcessing()

if __name__ == "__main__":
	main()