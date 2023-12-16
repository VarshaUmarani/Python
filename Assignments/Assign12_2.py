# Accept number of rows and number of columns from user and display below pattern. 

# Input : iRow = 4 iCol = 4 
# Output : 	A B C D 
# 			a b c d 
# 			A B C D 
# 			a b c d 

def Pattern(Row,Col):
    ch1 = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    ch2 = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
    'n','o','p','q','r','s','t','u','v','w','x','y','z']

    if Col <= 0 and Col > 26:
        return

    for i in range(1,(Row+1)):
        for j in range(Col):
            if i % 2 != 0:
            	print(ch1[j],end = "  ")
            else:
            	print(ch2[j],end = "  ")
        print()

def main():
    No1 = int(input("Enter Number of Rows : "))
    No2 = int(input("Enter Number of Columns : "))

    Pattern(No1,No2)

if __name__ == "__main__":
    main()