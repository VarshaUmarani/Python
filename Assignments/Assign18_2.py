# Accept N numbers from user and return difference between frequency of even number and odd numbers. 

# Input : N : 7 
# Elements : 85 66 3 80 93 88 90 
# Output : 1 (4 -3)

def DiffFrequency(list):
    Res1,Res2 = 0,0
    for i in range(len(list)):
        if list[i] % 2 == 0:
            Res1 = Res1 + 1
        else:
            Res2 = Res2 + 1
    return Res1 - Res2

def main():
    Arr = []
    Size = int(input("Enter Number of Elements : "))

    print("Enter Elements into list : ")
    for i in range(Size):
        Arr.append(int(input()))

    Ret = DiffFrequency(Arr)
    print("Difference of Frequency is :",Ret)

if __name__ == "__main__":
    main()