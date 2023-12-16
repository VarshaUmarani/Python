# Demonstration of sequence type i.e Set 

def main():
	# Duplicate entries are not stored in different memory, 
	# It will store only one element for duplicate entries
	arr = {10,20.5,"Hello",10}

	print(type(arr))
	print("Length of set is : ",len(arr))

	print(arr)

	for value in arr:
		print(value)

	if "Hello" in arr:
		print("Hello is there in arr.!")

	arr.add(20)
	print(arr)

	# remove() will remove specified element from set
	# It gives KeyError if the specified element is not present in set.
	arr.remove(20)
	print(arr)

	# discard() will remove specified element from set
	# It will not give error if the specified element is not present in set.
	# It is safer to use discard() in set to avoid the error
	arr.discard(20.5)
	print(arr)

	#pop() will delete last element of set
	# It is not a practical way to use pop() for set, because set is unordered.
	# So, which element will be deleted by pop() is unpredictable
	arr.pop()
	print(arr)

if __name__ == "__main__":
	main()