# Accept N numbers from user and display all such elements which are divisible by 5. 

# Input : N : 6 
# Elements : 85 66 3 80 93 88 
# Output : 85 80

def Accept(Size):
	Arr = []
	print("Enter Elements into list : ")
	for i in range(Size):
		Arr.append(int(input()))
	return Arr

def Display(Arr):
	for i in Arr:
		if i % 5 == 0:
			print(i,end = "  ")

def main():
	Size = int(input("Enter Number of Elements : "))

	list = Accept(Size)
	Display(list)

if __name__ == "__main__":
	main()