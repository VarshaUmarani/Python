# Demonstration of Dictionary
# Program to search the element from dictionary.

def main():
	books = {"C":"Programming approach in C","C++":"Thinking in C++","Java":"Java Programming","Python":"Learning Python","LSP":"Linux System Programming"}

	name = input("Enter the Language Name : ")

	# It will KeyError, if specified key is not present in dictionary
	print("Name of book is :",books[name])

if __name__ == "__main__":
	main()