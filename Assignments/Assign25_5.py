# Write a program which accept string from user reverse that string in place. 

# Input : “abcd” 
# Output : “dcba” 
# Input : “abba” 
# Output : “abba”

def Reverse_String(str):
	Str = str[::-1]
	return Str

def main():
	Str = input("Enter String : ")

	StrRev = Reverse_String(Str)
	print("Reversed String is :",StrRev)

if __name__ == "__main__":
	main()