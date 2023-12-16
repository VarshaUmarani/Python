# Accept N numbers from user and return frequency of 11 form it. 

# Input : N : 6 
# Elements : 85 66 3 15 93 88 
# Output : 0 

# Input : N : 6 
# Elements : 85 11 3 15 11 111 
# Output : 2

def Frequency(list):
    Result = 0
    for i in range(len(list)):
        if list[i] == 11:
            Result = Result + 1
    return Result

def main():
    Arr = []
    Size = int(input("Enter Number of Elements : "))

    print("Enter Elements into list : ")
    for i in range(Size):
        Arr.append(int(input()))

    Ret = Frequency(Arr)
    print("Frequency is :",Ret)

if __name__ == "__main__":
    main()