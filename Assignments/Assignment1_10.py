# Write a program which accept name from user and display length of its name.

# Input : Marvellous
# Output : 10

def CheckLength(Value):
	i = 0
	for char in Value:
		i = i + 1
	return i

def main():
	Name = input("Enter Name : ")

	Ret = CheckLength(Name)
	print("Length of {0} is : {1}".format(Name,Ret))

if __name__ == "__main__":
	main()