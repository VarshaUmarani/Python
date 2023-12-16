# Accept N numbers from user check whether that numbers contains 11 in it or not. 

# Input : N : 6 
# Elements : 85 66 11 80 93 88 
# Output : 11 is present 

# Input : N : 6 
# Elements : 85 66 3 80 93 88 
# Output : 11 is absent

def CheckNum(list,No):
    flag = 0
    for i in list:
        if i == No:
            flag = 1
            break
    if flag != 0:
        return True
    else:
        return False

def main():
    Arr = []
    Size = int(input("Enter Number of Elements : "))

    print("Enter Elements into list : ")
    for i in range(Size):
        Arr.append(int(input()))

    No = int(input("Enter Number to Search : "))

    bRet = CheckNum(Arr,No)
    if bRet == True:
        print("{} is Present in List".format(No))
    else:
        print("{} is not Present in List".format(No))

if __name__ == "__main__":
    main()