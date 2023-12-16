# Write a program which 2 strings from user and concat second string after first string. (Implement strcat() function). 

# Input : “Marvellous Infosystems” 
# “Logic Building” 
# Output : “Marvellous Infosystems Logic Building”

def String_Concat(Str1,Str2):
    Str = str(Str1)
    Str = Str + " "
    for s in Str2:
        Str = Str + s
    return Str

def main():
    str1 = input("Enter First String : ")
    str2 = input("Enter Second String : ")

    str = String_Concat(str1,str2)
    print("String After Concatenation is :",str)

if __name__ == "__main__":
    main()