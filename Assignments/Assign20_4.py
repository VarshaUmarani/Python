# Accept N numbers from user and display all such numbers which contains 3 digits in it. 

# Input : N : 6  
# Elements : 8225 665 3 76 953 858 
# Output : 665 953 858 

def Display(list):
    Digit = 0
    for i in list:
        Cnt = 0
        No = i
        while No != 0:
            Digit = int(No % 10)
            Cnt = Cnt + 1
            No = int(No / 10)

        if Cnt == 3:
            print(i,end = "  ")

def main():
    Arr = []
    Size = int(input("Enter Number of Elements : "))

    print("Enter Elements into list : ")
    for i in range(Size):
        Arr.append(int(input()))

    Display(Arr)

if __name__ == "__main__":
    main()