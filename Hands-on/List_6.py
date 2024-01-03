# Accept N numbers from user and return the Addition of those Numbers.
# Using while loop

# Input  : 10 20 30 40 50
# Output : 150

def Addition(LIST):
	Sum = 0
	i = 0

	while i < len(LIST):
		Sum = Sum + LIST[i]
		i = i + 1

	return Sum

def main():
	Arr = []

	print("Enter the Number of Elements : ")
	Size = int(input())

	for i in range(Size):
		print("Enter Element at {} :".format(i+1))
		# Arr.append(int(input()))
		Value = int(input())
		Arr.append(Value)

	print("Accepted data is :",Arr)

	Ret = Addition(Arr)
	print("Addition of all the element is :",Ret)

if __name__ == "__main__":
	main()