# Accept number of rows and number of columns from user and display below pattern. 

# Input : iRow = 6 iCol = 5  
# Output :  * * * * * 
#           * @ @ @ * 
#           * @ @ @ * 
#           * @ @ @ * 
#           * @ @ @ * 
#           * * * * *

def PrintStar():
    print("*",end = "  ")

def PrintSign():
    print("@",end = "  ")

def Pattern(Row,Col):
    for i in range(1,(Row+1)):
        for j in range(1,(Col+1)):
            if i == 1 or i == Row or j == 1 or j == Col:
                PrintStar()
            else:
                PrintSign()
        print()

def main():
    No1 = int(input("Enter Number of Rows : "))
    No2 = int(input("Enter Number of Columns : "))

    Pattern(No1,No2)

if __name__ == "__main__":
    main()