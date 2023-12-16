# Write a program which accept string from user and copy capital characters of that string into another string. 

# Input : “Marvellous Multi OS” 
# Output : “MMOS” 

def String_Copy(Str):
    Str1 = ""
    for s in Str:
    	if s >= 'A' and s <= 'Z':
    		Str1 = Str1 + str(s)
    return Str1

def main():
    Str = input("Enter String : ")

    StrCpy = String_Copy(Str)
    print("Copied String is :",StrCpy)

if __name__ == "__main__":
    main()