# Write a program which accept number from user and print even factors of that number. 

# Input : 36 
# Output: 2 6 12 18

def EvenFactors(No):
    for i in range(1,int(No/2)+1):
        if No % i == 0 and i % 2 == 0:
            print(i,end = "  ")

def main():
    Num = int(input("Enter Number : "))

    EvenFactors(Num)

if __name__ == "__main__":
    main()