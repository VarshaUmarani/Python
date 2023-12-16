# Accept N numbers from user and accept one another number as NO , check whether NO is present or not. 

# Input : N : 6 
# NO: 66 
# Elements : 85 66 3 66 93 88 
# Output : TRUE 

# Input : N : 6 
# NO: 12 
# Elements : 85 11 3 15 11 111 
# Output : FALSE

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