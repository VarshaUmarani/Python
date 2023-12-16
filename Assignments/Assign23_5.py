# Write a program which accept string from user and display it in reverse order. 

# Input : “MarvellouS” 
# Output : “SuollevraM”

def Reverse_String(str):
    Str = str[::-1]
    print(Str)

def main():
    Str = input("Enter String : ")

    Reverse_String(Str)

if __name__ == "__main__":
    main()