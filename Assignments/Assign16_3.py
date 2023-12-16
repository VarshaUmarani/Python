# Accept number of rows and number of columns from user and display below pattern. 

# Input : iRow = 6 iCol = 6 
# Output :  * * * * * *    6,1   6,2   6,3  6,4  6,5  6,6
#           *       * *    5,1   5,2   5,3  5,4  5,5  5,6
#           *     *   *    4,1   4,2   4,3  4,4  4,5  4,6
#           *   *     *    3,1   3,2   3,3  3,4  3,5  3,6
#           * *       *    2,1   2,2   2,3  2,4  2,5  2,6
#           * * * * * *    1,1   1,2   1,3  1,4  1,5  1,6

def PrintStar():
    print("*", end = "      ")

def Pattern(Row,Col):
    if Row != Col:
        return

    for i in range(Row,0,-1):
        for j in range(1,Col+1):
            if i == 1 or i == Row or j == 1 or j == Col or i == j:
                PrintStar()
            else:
                print(end = "       ")
        print()

def main():
    No1 = int(input("Enter Number of Rows : "))
    No2 = int(input("Enter Number of Columns : "))

    Pattern(No1,No2)

if __name__ == "__main__":
    main()