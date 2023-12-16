# Write application which accept two file names from user. Append the contents of first file at the end of second file. 

# Input : Demo.txt Hello.txt 
# Output : Concat contents of Demo.txt at the end of Hello.txt

def append_file(name1, name2):
    try:
        with open(name1, 'rb') as file1, open(name2, 'ab') as file2:
            print("Both the Files Opened Successfully..!!!")
            content = file1.read()
            file2.write(content)

    except FileNotFoundError:
        print("Error : File Not Found")

def main():
    file1 = input("Enter First File Name : ")
    file2 = input("Enter Second File Name : ")

    append_file(file1, file2)

if __name__ == "__main__":
    main()