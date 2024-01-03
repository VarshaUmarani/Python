# Demonstration of Dictionary

def main():
	books = {"C":"Programming approach in C","C++":"Thinking in C++","Java":"Java Programming","Python":"Learning Python"}

	print("Type of books is : ",type(books))
	print("Length of Dictionary is : ",len(books))

	print(books)
	print(books["C"])
	print(books["C++"])
	print(books["Java"])
	print(books["Python"])

if __name__ == "__main__":
	main()