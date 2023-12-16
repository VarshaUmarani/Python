# Write application which accept file name and one character from user. Count the frequency of that character in file. 

# Input : Demo.txt 
# M 
# Output : Count occurrence of M in Demo.txt

def frequency(file_name, char_value):
    try:
        with open(file_name, 'r') as file:
            print("File Opened Successfully..!!!")
            content = file.read()
            count = content.count(char_value)

    except FileNotFoundError:
        print("Error : File Not Found")
        return -1

    return count

def main():
    file_name = input("Enter File Name : ")
    char_value = input("Enter a Character : ")

    if len(char_value) != 1:
        print("Please enter a single character.")
    else:
        result = frequency(file_name, char_value)

        if result != -1:
            print(f"Occurrence of {char_value} in the given file is: {result}")

if __name__ == "__main__":
	main()