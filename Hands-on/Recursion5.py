# Accept N numbers from user and find addition of all that N numbers.
# Using Recursive method

# Size : 7
# Input : [1,3,2,4,6,5,4]
# Output : 25

Add = 0
i = 0

def Addition(List):
	global Add,i
	if i != len(List):
		Add = Add + List[i]
		i = i + 1
		Addition(List)

	return Add

def main():
	Arr = []

	Size = int(input("Enter Number of Elements : "))

	for i in range(Size):
		# 1st Way : No = int(input()) 	
		# Arr.append(No)
		# 2nd Way : Arr.append(int(input()))
		Arr.append(int(input("Enter Element Number {} : ".format(i+1))))

	print("Entered Elements are : ",Arr)

	Ret = Addition(Arr)
	print("Addition of all the Elements is : ",Ret)

if __name__ == "__main__":
	main()