# Accept N numbers from user and return the largest number. 

# Input : N : 6 
# Elements : 85 66 3 66 93 88 
# Output : 93 

def Maximum(list):
    Max = 0
    for i in list:
        if i > Max:
            Max = i
    return Max

def main():
    Arr = []
    Size = int(input("Enter Number of Elements : "))

    print("Enter Elements into list : ")
    for i in range(Size):
        Arr.append(int(input()))

    Ret = Maximum(Arr)
    print("Maximum in list is :",Ret)

if __name__ == "__main__":
    main()