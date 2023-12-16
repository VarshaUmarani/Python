# Accept N numbers from user and return product of all odd elements. 

# Input : N : 6 
# Elements : 15 66 3 70 10 88 
# Output : 45 

# Input : N : 6 
# Elements : 44 66 72 70 10 88 
# Output : 0 

def Product(list):
    Result = 1
    Cnt = 0
    for i in list:
        if i % 2 != 0:
            Cnt = Cnt + 1
            Result = Result * i
    if Cnt == 0:
        return -1
    else:
        return Result

def main():
    Arr = []
    Size = int(input("Enter Number of Elements : "))

    print("Enter Elements into list : ")
    for i in range(Size):
        Arr.append(int(input()))

    Ret = Product(Arr)
    if Ret == -1:
        print("There are No Odd Elements in List...!!!")
    else:
        print("Product of Odd Elements in list is :",Ret)

if __name__ == "__main__":
    main()