# Accept N numbers from user and return the largest number. 

# Input : N : 6 
# Elements : 85 66 3 66 93 88 
# Output : 93 

from array import *

def MaximumNumber(Arr):
	Max = Arr[0]

	for i in range(1,len(Arr)):
		if Arr[i] > Max:
			Max = Arr[i]

	return Max

def main():
	Size = int(input("Enter Number of Elements : "))

	Arr = array('i',[Size])

	print("Enter Elements into Array : ")
	for i in range(Size):
		Arr.append(int(input()))

	ret = MaximumNumber(Arr)
	print("Maximum Number is : ",ret)

if __name__ == "__main__":
	main()