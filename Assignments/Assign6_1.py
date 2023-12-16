# Write a program which accept number from user and display its digits in reverse order.

# Input : 2395 
# Output : 5 
#          9 
#          3 
#          2

# Input : 1018 
# Output : 8 
#          1 
#          0 
#          1 

# Input : -1018 
# Output : 8 
#          1 
#          0 
#          1 

# Input : 9000 
# Output : 0 
#          0 
#          0 
#          9 

def DisplayDigits(No):
    Digit = 0

    while No != 0:
        Digit = No % 10
        print(Digit)
        No = int(No / 10)

def main():
    Num = int(input("Enter Number : "))

    DisplayDigits(Num)

if __name__ == "__main__":
    main()