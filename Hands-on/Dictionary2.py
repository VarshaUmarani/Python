# Demonstration of Dictionary
# Program to add new element into the dictionary and traversing the dictionary.

def main():
	books = {"C":"Programming approach in C","C++":"Thinking in C++","Java":"Java Programming","Python":"Learning Python"}
	
	# We can add new element into dictionary
	books["LSP"] = "Linux System Programming with UNIX Internals"

	print("Key of dictionary : ")
	for key in books.keys():
		print(key)

	print("Values of dictionary : ")
	for value in books.values():
		print(value)

	print("Keys ans Values of dictionary : ")
	for value in books.keys():
		print("{} : {}".format(value,books[value]))

	print("Keys ans Values of dictionary : ")
	for i,j in books.items():
		print("{} : {}".format(i,j))

if __name__ == "__main__":
	main()