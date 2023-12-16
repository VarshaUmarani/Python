# Write a program which accept string from user and accept one character. Check whether that character is present in string or not. 

# Input : “Marvellous Multi OS” 
# e 
# Output : TRUE 

# Input : “Marvellous Multi OS” 
# W 
# Output : FALSE 

def Check_Character(str,ch):
    flag = 0
    for s in str:
        if s == ch:
            flag = 1
            break
    if flag != 0:
        return True
    else:
        return False

def main():
    Str = input("Enter String : ")
    Ch = input("Enter Character : ")

    bRet = Check_Character(Str,Ch)
    if bRet == True:
        print("%s is Present in %s"%(Ch,Str))
    else:
        print("%s is Not Present in %s"%(Ch,Str))

if __name__ == "__main__":
    main()