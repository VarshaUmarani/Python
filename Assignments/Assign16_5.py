# Accept number of rows and number of columns from user and display below pattern. 

# Input : iRow = 4 iCol = 4 
# Output :  1 2 3 4 5 
#           1 2     5 
#           1   3   5 
#           1     4 5 
#           1 2 3 4 5

def Pattern(Row,Col):
    if Row != Col:
        return

    for i in range(1,(Row+1)):
        for j in range(1,(Col+1)):
            if i == 1 or i == Row or j == 1 or j == Col or i == j:
                print(j,end = "     ")
            else:
                print(end = "      ")
        print()

def main():
    No1 = int(input("Enter Number of Rows : "))
    No2 = int(input("Enter Number of Columns : "))

    Pattern(No1,No2)

if __name__ == "__main__":
    main()