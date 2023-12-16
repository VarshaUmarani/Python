# Implementation of Parallel Processing

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

def main():
	ParallelProcessing()

if __name__ == "__main__":
	main()