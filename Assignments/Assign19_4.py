# Accept N numbers from user and accept Range, Display all elements from that range 

# Input : N : 6 
# Start: 60  
# End : 90 
# Elements : 85 66 3 76 93 88 
# Output : 85 66 76 88 

# Input : N : 6 
# Start: 30 
# End : 50 
# Elements : 85 66 3 76 93 88 
# Output :

def DisplayRange(list,Start,End):
    if Start > End:
        return
    for i in range(len(list)):
        if list[i] >= Start and list[i] <= End:
            print(list[i],end = "  ")

def main():
    Arr = []
    Size = int(input("Enter Number of Elements : "))

    print("Enter Elements into a list : ")
    for i in range(Size):
        Arr.append(int(input()))

    No1 = int(input("Enter Starting Range : "))
    No2 = int(input("Enter Ending Range : "))

    DisplayRange(Arr,No1,No2)

if __name__ == "__main__":
    main()