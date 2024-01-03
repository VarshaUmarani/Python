# Implementation of Serial Processing

import os
import time

def Square(no):
	return no ** 2

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
	SerialProcessing()

if __name__ == "__main__":
	main()