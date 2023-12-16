# Accept N numbers from user and display summation of digits of each number. 

# Input : N : 6 
# Elements : 8225 665 3 76 953 858 
# Output : 17 17 3 13 17 21 

def Display(list):
    for i in list:
        Digit = 0
        Sum = 0
        No = i
        while No != 0:
            Digit = int(No % 10)
            Sum = Sum + Digit
            No = int(No / 10)

        print(Sum,end = "  ")

def main():
    Arr = []
    Size = int(input("Enter Number of Elements : "))

    print("Enter Elements into list : ")
    for i in range(Size):
        Arr.append(int(input()))

    Display(Arr)

if __name__ == "__main__":
    main()