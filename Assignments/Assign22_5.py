# Accept character from user and display its ASCII value in decimal, octal and hexadecimal format. 

# Input : A 
# Output : Decimal 65 
# Octal 0101 
# Hexadecimal 0X41

def DisplayASCII(Ch):
    print("Value :",Ch)
    print("Decimal :",ord(Ch))
    print("Octal :",oct(ord(Ch)))
    print("Hexadecimal :",hex(ord(Ch)))

def main():
    Ch = input("Enter Character : ")

    DisplayASCII(Ch)

if __name__ == "__main__":
    main()