# Demonstration of Tuple in Python

def main():
	tuple = (11,21,23.5,"Hello World..!!")

	print("Type is : ",type(tuple))
	print("Length is : ",len(tuple))

	for i in range(len(tuple)):
		print(tuple[i])

	# TypeError: 'tuple' object does not support item assignment
	# tuple doesn't allow to change the value of element, because tuple is immutable 
	# tuple[0] = 12

if __name__ == "__main__":
	main()