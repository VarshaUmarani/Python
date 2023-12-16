# Write a program which accept string from user and copy the contents of that string into another string. 
# (Implement strncpy() function) 

# Input : “Marvellous Multi OS” 
# 10 
# Output : “Marvellous 

def String_Copy(Str):
    Str1 = str(Str)
    return Str1

def main():
    Str = input("Enter String : ")

    StrCpy = String_Copy(Str)
    print("Copied String is :",StrCpy)

if __name__ == "__main__":
    main()