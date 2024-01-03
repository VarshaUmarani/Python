import sys

def main():
	a = 11
	print("Value of a is : ",a)
	print("Data type of a is : ",type(a))
	print("Size of a is : ",sys.getsizeof(a))

	b = 11 ** 3
	print("Value of b is : ",b)
	print("Data type of a is : ",type(b))
	print("Size of b is : ",sys.getsizeof(b))

if __name__ == "__main__":
	main()