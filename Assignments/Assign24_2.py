# Write a program which accept string from user and convert it into upper case. 

# Input : “Marvellous Multi OS” 
# Output : MARVELLOUS MULTI OS

def Upper_String(Str):
	Str = Str.upper()
	print(Str)

def main():
	str = input("Enter String : ")

	Upper_String(str)

if __name__ == "__main__":
	main()