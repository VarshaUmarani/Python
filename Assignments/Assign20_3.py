# Accept N numbers from user and return the difference between largest and smallest number. 

# Input : N : 6 
# Elements : 85 66 3 66 93 88 
# Output : 90 (93 -3) 

def Difference(list):
    Min = list[0]
    Max = 0

    for i in list:
        if i > Max:
            Max = i
        elif i < Min:
            Min = i
    return Max - Min

def main():
    Arr = []
    Size = int(input("Enter Number of Elements : "))

    print("Enter Elements into list : ")
    for i in range(Size):
        Arr.append(int(input()))

    Ret = Difference(Arr)
    print("Difference in list is :",Ret)

if __name__ == "__main__":
    main()