# Default Recursion limit in Python is : 1000 times
# We can set a new limit for recursion using setrecursionlimit() function from sys module.

import sys

def main():
	print("Recursion Limit is : ",sys.getrecursionlimit())

	sys.setrecursionlimit(100)
	print("New Recursion Limit is : ",sys.getrecursionlimit())

if __name__ == "__main__":
	main()