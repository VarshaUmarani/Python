# Accept number of rows and number of columns from user and display below pattern. 

# Input : iRow = 3 iCol = 5 
# Output :  A A A A A 
#           B B B B B 
#           C C C C C

def Pattern(Row,Col):
    ch = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    if Col <= 0 and Col > 26:
        return

    for i in range(Row):
        for j in range(Col):
            print(ch[i],end = "  ")
        print()

def main():
    No1 = int(input("Enter Number of Rows : "))
    No2 = int(input("Enter Number of Columns : "))

    Pattern(No1,No2)

if __name__ == "__main__":
    main()