# Accept number of rows and number of columns from user and display below pattern. 

# Input : iRow = 4 iCol = 4 
# Output :  * # # # 
#           * * # # 
#           * * * # 
#           * * * * 

def PrintStar():
    print("*",end = "  ")

def PrintHash():
    print("#",end = "  ")

def Pattern(Row,Col):
    if Row != Col:
        return
    for i in range(1,(Row+1)):
        for j in range(1,(Col+1)):
            if i >= j:
                PrintStar()
            else:
                PrintHash()
        print()

def main():
    No1 = int(input("Enter Number of Rows : "))
    No2 = int(input("Enter Number of Columns : "))

    Pattern(No1,No2)

if __name__ == "__main__":
    main()