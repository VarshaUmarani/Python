# Write application which accept file name from user and one string from user. Write that string at the end of file. 

# Input : Demo.txt 
# Hello World 
# Output : Write Hello World at the end of Demo.txt file

def Write_File(Name,Str):
    try:
        fobj = open(Name,"a")
        fobj.write(Str)
    except Exception as e:
        print("No File Named ",Name)
        return

def main():
    name = input("Enter File Name : ")
    Str = input("Enter String : ")

    Write_File(name,Str)

if __name__ == "__main__":
    main()