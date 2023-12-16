# Write a program which accept string from user and copy the contents of that string into another string. 
# (Implement strcpy() function) 

# Input : “Marvellous Multi OS” 
# Output : “Marvellous Multi OS” in another string

def String_Copy(Str):
	Str1 = str(Str)
	return Str1

def main():
	Str = input("Enter String : ")

	StrCpy = String_Copy(Str)
	print("Copied String is :",StrCpy)

if __name__ == "__main__":
	main()