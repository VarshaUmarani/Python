# Accept number from user and display below pattern. 

# Input : 5 
# Output : A B C D E 

def Pattern(No):
    ch = 'A'

    if No > 26 or No <= 0:
        print("Invalid Input...!!!")
        return

    for i in range(No):
        print(ch,end = "  ")
        ch = chr(ord(ch) + 1)

def main():
    print("Enter Number : ")
    Num = int(input())

    Pattern(Num)

if __name__ == "__main__":
    main()