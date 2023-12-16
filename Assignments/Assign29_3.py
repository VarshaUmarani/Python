# Write a program which accept one number and position from user and on that bit. Return modified number. 

# Input : 10 3 
# Output : 14

def ON_Bit(Value,Pos):
    if Pos <= 0 or Pos > 32:
        print("Invalid Input...")
        return

    Mask = 0x00000001

    Mask = Mask << (Pos - 1)

    Num = Value | Mask
    return Num

def main():
    No = int(input("Enter Number : "))
    Pos = int(input("Enter Position : "))

    Ret = ON_Bit(No,Pos)
    print("Modified Number is :",Ret)

if __name__ == "__main__":
    main()