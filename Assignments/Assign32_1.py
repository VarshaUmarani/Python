# Write application which accept two file names from user. Compare the contents of that two files.
# If contents are same then return true otherwise return false. 

# Input : Demo.txt Hello.txt 
# Output : Compare contents of Demo.txt and Hello.txt

def compare_data(file_name1, file_name2):
    flag = 0

    try:
        with open(file_name1, 'rb') as f1, open(file_name2, 'rb') as f2:
            print("Both the Files Opened Successfully..!!!")
            
            while True:
                byte1 = f1.read()
                byte2 = f2.read()

                if not byte1 or not byte2:
                    break

                if byte1 != byte2:
                    flag = 1
                    break

        if flag != 1:
            return True
        else:
            return False

    except FileNotFoundError:
        print("Unable to Open file..!!!")

def main():
    file1 = input("Enter First File Name : ")
    file2 = input("Enter Second File Name : ")

    result = compare_data(file1, file2)

    if result:
        print("Contents of both the files are same..!!!")
    elif result == False:
        print("Contents of both the files are different..!!!")
    else:
        print("Error : File Not Found")

if __name__ == "__main__":
    main()
