# Accept N numbers from user and accept one another number as NO , return frequency of NO form it. 

# Input : N : 6 
# NO: 66 
# Elements : 85 66 3 66 93 88 
# Output : 2 

# Input : N : 6 
# NO: 12 
# Elements : 85 11 3 15 11 111 
# Output : 0 

def Frequency(list,No):
    Result = 0

    for i in list:
        if i == No:
            Result = Result + 1
    return Result

def main():
    Arr = []
    Size = int(input("Enter Number of Elements : "))

    print("Enter Elements into list : ")
    for i in range(Size):
        Arr.append(int(input()))

    No = int(input("Enter Number to Search : "))

    Ret = Frequency(Arr,No)
    print("Frequency of {} in list is : {}".format(No,Ret))

if __name__ == "__main__":
    main()