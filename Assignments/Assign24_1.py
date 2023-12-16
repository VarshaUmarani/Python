# Write a program which accept string from user and convert it into lower case. 

# Input : “Marvellous Multi OS” 
# Output : marvellous multi os

def Lower_String(str):
	str = str.lower()
	print(str)

def main():
	Str = input("Enter String : ")

	Lower_String(Str)

if __name__ == "__main__":
	main()