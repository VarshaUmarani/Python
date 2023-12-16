# Accept N numbers from user and display all such elements which are divisible by 3 and 5. 

# Input : N : 6 
# Elements : 85 66 3 15 93 88 
# Output : 15 

def Accept(Size):
    Arr = []
    print("Enter Elements into a list : ")
    for i in range(Size):
        Arr.append(int(input()))
    return Arr

def Display(list):
    for i in list:
        if i % 3 == 0 and i % 5 == 0:
            print(i,end = "  ")

def main():
    Size = int(input("Enter Number of Elements : "))

    list = Accept(Size)
    Display(list)

if __name__ == "__main__":
    main()