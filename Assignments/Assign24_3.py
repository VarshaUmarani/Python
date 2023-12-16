# Write a program which accept string from user and toggle the case. 

# Input : “Marvellous Multi OS” 
# Output : mARVELLOUS mULTI os

def Toggle_String(str):
	str = str.swapcase()
	print(str)

def main():
	Str = input("Enter String : ")

	Toggle_String(Str)

if __name__ == "__main__":
	main()