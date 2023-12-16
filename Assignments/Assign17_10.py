# Accept N numbers from user and display all such elements which are multiples of 11. 

# Input : N : 6 
# Elements : 85 66 3 55 93 88 
# Output : 66 55 88

def Accept(Size):
    Arr = []
    print("Enter Elements into a list : ")
    for i in range(Size):
        Arr.append(int(input()))
    return Arr

def Display(list):
    for i in list:
        if i % 11 == 0:
            print(i,end = "  ")

def main():
    Size = int(input("Enter Number of Elements : "))

    list = Accept(Size)
    Display(list)

if __name__ == "__main__":
    main()