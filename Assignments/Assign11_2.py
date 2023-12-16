# Accept number of rows and number of columns from user and display below pattern. 

# Input : iRow = 4 iCol = 3 
# Output : 1 2 3 
#          1 2 3 
#          1 2 3 
#          1 2 3 

def Pattern(Row,Col):
    for i in range(1,Row+1):
        for j in range(1,Col+1):
            print(j,end = "  ")
        print()

def main():
    No1 = int(input("Enter Number of Rows : "))
    No2 = int(input("Enter Number of Columns : "))

    Pattern(No1,No2)

if __name__ == "__main__":
    main()