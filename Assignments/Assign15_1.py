# Accept number of rows and number of columns from user and display below pattern. 

# Input : iRow = 4 iCol = 4 
# Output :  * 
#           * * 
#           * * * 
#           * * * *

def PrintStar():
    print("*",end = "  ")

def Pattern(Row,Col):
    if Row != Col:
        return

    for i in range(Row):
        for j in range(Col):
            if i >= j:
                PrintStar()
            else:
                pass
        print()

def main():
    No1 = int(input("Enter Number of Rows : "))
    No2 = int(input("Enter Number of Columns : "))

    Pattern(No1,No2)

if __name__ == "__main__":
    main()