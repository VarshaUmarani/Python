# Write a program which accept string from user and accept one character. Return frequency of that character. 

# Input : “Marvellous Multi OS” 
# M 
# Output : 2 

# Input : “Marvellous Multi OS” 
# W 
# Output : 0 

def Char_Frequency(str,ch):
    Cnt = 0
    for s in str:
        if s == ch:
            Cnt = Cnt + 1
    return Cnt

def main():
    Str = input("Enter String : ")
    Ch = input("Enter Character : ")

    Ret = Char_Frequency(Str,Ch)
    print("Frequency of %s in %s is : %d"%(Ch,Str,Ret))

if __name__ == "__main__":
    main()