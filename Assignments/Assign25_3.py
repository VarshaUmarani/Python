# Write a program which accept string from user and accept one character. Return index of first occurrence of that character. 

# Input : “Marvellous Multi OS”
# M
# Output : 0

# Input : “Marvellous Multi OS”
# W
# Output : -1

# Input : “Marvellous Multi OS”
# e
# Output : 4

def First_Occurance(str,ch):
    i = 0
    flag = 0
    for s in str:
        if s == ch:
            flag = 1
            break
        i = i + 1
    if flag != 1:
        return -1
    else:
        return i

def main():
    Str = input("Enter String : ")
    Ch = input("Enter Character : ")

    Ret = First_Occurance(Str,Ch)
    if Ret == -1:
        print("There is No Such Character in String...!!!")
    else:
        print("First Occurance of %s in %s is : %d"%(Ch,Str,Ret))

if __name__ == "__main__":
    main()