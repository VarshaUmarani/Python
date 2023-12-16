# Accept number of rows and number of columns from user and display below pattern. 

# Input : iRow = 4 iCol = 5 
# Output :  4 4 4 4 4 
#           3 3 3 3 3 
#           2 2 2 2 2 
#           1 1 1 1 1 

def Pattern(Row,Col):
    for i in range(Row,0,-1):
        for j in range(Col):
            print(i,end = "  ")
        print()

def main():
    No1 = int(input("Enter Number of Rows : "))
    No2 = int(input("Enter Number of Columns : "))

    Pattern(No1,No2)

if __name__ == "__main__":
    main()