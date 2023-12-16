# Demonstration of Dictionary
# Program to search the element from dictionary.

def main():
	books = {"C":"Programming approach in C","C++":"Thinking in C++","Java":"Java Programming","Python":"Learning Python","LSP":"Linux System Programming"}

	print("Enter the Language Name : ")
	name = input()

	# get() will return the value of specified key from dictionary.
	# If key is not present in dictionary, it will return None
	# To avoid getting result as None, we can pass the parameter to get() as
	print(books.get(name,"There is no such Language present in dictionary.!"))

if __name__ == "__main__":
	main()