# Accept number of rows and number of columns from user and display below pattern. 

# Input : iRow = 3 iCol = 5 
# Output : 
# 5 4 3 2 1 
# 5 4 3 2 1 
# 5 4 3 2 1 

def Pattern(Row,Col):
    for i in range(Row):
        for j in range(Col,0,-1):
            print(j,end = "  ")
        print()

def main():
    No1 = int(input("Enter Number of Rows : "))
    No2 = int(input("Enter Number of Columns : "))

    Pattern(No1,No2)

if __name__ == "__main__":
    main()