# Accept number of rows and number of columns from user and display below pattern. 

# Input : iRow = 3 iCol = 4 
# Output :  1 2 3 4 
#           5 6 7 8 
#           9 10 11 12

def Pattern(Row,Col):
    Cnt = 0
    for i in range(Row):
        for j in range(Col):
            Cnt = Cnt + 1
            print(Cnt,end = "   ")
        print()

def main():
    No1 = int(input("Enter Number of Rows : "))
    No2 = int(input("Enter Number of Columns : "))

    Pattern(No1,No2)

if __name__ == "__main__":
    main()