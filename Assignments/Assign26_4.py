# Write a program which accept string from user and copy small characters of that string into another string. 

# Input : “Marvellous multi OS” 
# Output : “arvellous multi” 

def Copy_Small(str):
	Str = ""
	for s in str:
		if s >= 'a' and s <= 'z':
			Str = Str + s
	return Str

def main():
	str = input("Enter String : ")

	Str = Copy_Small(str)
	print("Copied String is :",Str)

if __name__ == "__main__":
	main()