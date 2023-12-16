# Write a program which accept string from user and accept one character. Return index of last occurrence of that character. 

# Input : “Marvellous Multi OS” 
# M 
# Output : 11 

# Input : “Marvellous Multi OS” 
# W 
# Output : -1 

# Input : “Marvellous Multi OS” 
# e 
# Output : 4

def Last_Occurance(str,ch):

    Str = str[::-1]
    i = len(Str) - 1
    flag = 0
    for s in Str:
        if s == ch:
            flag = 1
            break
        i = i - 1
    if flag != 1:
        return -1
    else:
        return i

def main():
    Str = input("Enter String : ")
    Ch = input("Enter Character : ")

    Ret = Last_Occurance(Str,Ch)
    if Ret == -1:
        print("There is No Such Character in String...!!!")
    else:
        print("Last Occurance of %s in %s is : %d"%(Ch,Str,Ret))

if __name__ == "__main__":
    main()