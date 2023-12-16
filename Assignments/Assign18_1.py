# Accept N numbers from user and return frequency of even numbers. 

# Input : N : 6 
# Elements : 85 66 3 80 93 88 
# Output : 3 

def Frequency(list):
    Result = 0
    for i in range(len(list)):
        if list[i] % 2 == 0:
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