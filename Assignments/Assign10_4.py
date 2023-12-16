# Accept number from user and display below pattern. 

# Input : 4 
# Output : # 1 * # 2 * # 3 * # 4 * 

def DisplayPattern(No):
    for i in range(1,(No+1)):
        print("#  {}  *".format(i),end = "  ")

def main():
    Num = int(input("Enter Number : "))

    DisplayPattern(Num)

if __name__ == "__main__":
    main()