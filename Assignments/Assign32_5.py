# Accept three file names from user which are existing files. Create one new file named as Demo.txt.
# Write name and Data of that three files in Demo.txt file one after another.

# Input : abc.txt 
# pqr.txt 
# xyz.txt 
# Output : Write file name and data of each file in Demo.txt file. 

def create_file(name1, name2, name3):
    try:
        with open("Demo.txt", 'w') as file:
            print(f"{file.name} File Opened Successfully...!!!")

        with open(name1, 'r') as file1, open(name2, 'r') as file2, open(name3, 'r') as file3, open("Demo.txt", 'a') as demo_file:
            content = file1.read()
            demo_file.write(content)

            content = file2.read()
            demo_file.write(content)

            content = file3.read()
            demo_file.write(content)

    except FileNotFoundError:
        print("Error : File Not Found")

def main():
    file_name1 = input("Enter First File Name : ")
    file_name2 = input("Enter Second File Name : ")
    file_name3 = input("Enter Third File Name : ")

    create_file(file_name1, file_name2, file_name3)

if __name__ == "__main__":
    main()