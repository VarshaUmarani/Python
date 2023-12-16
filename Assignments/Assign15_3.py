# Accept number of rows and number of columns from user and display below pattern. 

# Input : iRow = 5 iCol = 5 
# Output :  $ * * * *   1,1  1,2  1,3  1,4  1,5
#           # $ * * *   2,1  2,2  2,3  2,4  2,5
#           # # $ * *   3,1  3,2  3,3  3,4  3,5
#           # # # $ *   4,1  4,2  4,3  4,4  4,5
#           # # # # $   5,1  5,2  5,3  5,4  5,5

def PrintStar():
    print("*",end = "  ")

def PrintHash():
    print("#",end = "  ")

def PrintDollar():
    print("$",end = "  ")

def Pattern(Row,Col):
    if Row != Col:
        return

    for i in range(Row):
        for j in range(Col):
            if i < j:
                PrintStar()
            elif i == j:
                PrintDollar()
            else:
                PrintHash()
        print()

def main():
    No1 = int(input("Enter Number of Rows : "))
    No2 = int(input("Enter Number of Columns : "))

    Pattern(No1,No2)

if __name__ == "__main__":
    main()