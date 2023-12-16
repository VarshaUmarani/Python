# Write a program which accept string from user and count number of white spaces 

# Input : “MarvellouS” 
# Output : 0 

# Input : “MarvellouS Infosystems” 
# Output : 1 

# Input : “MarvellouS Infosystems by Piyush Manohar Khairnnar” 
# Output : 5

def Count_Spaces(str):
    Cnt = 0
    for c in str:
        if c == ' ':
            Cnt = Cnt + 1
    return Cnt

def main():
    Str = input("Enter String : ")

    Ret = Count_Spaces(Str)
    print("Count of White Spaces is :",Ret)

if __name__ == "__main__":
    main()