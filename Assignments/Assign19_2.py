# Accept N numbers from user and accept one another number as NO , return index of first occurrence of that NO. 

# Input : N : 6 
# NO: 66 
# Elements : 85 66 3 66 93 88 
# Output : 1 

# Input : N : 6 
# NO: 12 
# Elements : 85 11 3 15 11 111 
# Output : -1

def FirstIndex(list,No):
    flag = 0
    for i in range(len(list)):
        if list[i] == No:
            flag = 1
            break

    if flag == 0:
        return -1
    else:
        return i

def main():
    Arr = []
    Size = int(input("Enter Number of Elements : "))

    print("Enter Elements into a list : ")
    for i in range(Size):
        Arr.append(int(input()))

    No = int(input("Enter Number to Search : "))

    Ret = FirstIndex(Arr,No)
    if Ret == -1:
        print("There is no such element...!!!")
    else:
        print("First Index of {} is : {}".format(No,Ret))

if __name__ == "__main__":
    main()