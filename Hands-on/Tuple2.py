# Demonstration of Tuple in Python

def main():
	tuple1 = (10,20,30)
	print("type of tuple1 is : ",type(tuple1))	# <class 'tuple'>

	tuple2 = (10)
	print("type of tuple2 is : ",type(tuple2))	# <class 'int'>

	# Writing , is necessary while creating the tuple, if the tuple will be growing after the creation.
	# If we don't write , in this case, then tuple3 will be considered as object of class int
	tuple3 = (10,)
	print("type of tuple3 is : ",type(tuple3))	# <class 'tuple'>

if __name__ == "__main__":
	main()