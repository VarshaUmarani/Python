# Demonstration of sequence type i.e Set 
# We cannot change the value of element in set directly.

def main():
	arr = {10,20,30,40}
	print(type(arr))

	temp = list(arr)
	print(type(temp))

	temp[1] = 21
	arr = set(temp)
	print(arr)

if __name__ == "__main__":
	main()