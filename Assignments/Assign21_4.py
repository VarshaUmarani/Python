# Accept Character from user and check whether it is small case or not (a-z). 

# Input : g 
# Output : TRUE 

# Input : D 
# Output : FALSE 

def CheckSmall(Ch):
    if Ch >= 'a' and Ch <= 'z':
        return True
    else:
        return False

def main():
    Ch = input("Enter Character : ")

    bRet = CheckSmall(Ch)

    if bRet == True:
        print("{} is a Small Case".format(Ch))
    else:
        print("{} is Not Small Case".format(Ch))

if __name__ == "__main__":
    main()