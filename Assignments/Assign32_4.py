# Write application which accept file name and one word from user. Count the frequency of that word in file. 

# Input : Marvellous.txt 
# Hello 
# Output : Count the frequency of Hello in Marvellous.txt file. 

def word_frequency(file_name, word):
    try:
        with open(file_name, 'r') as file:
            print("File Opened Successfully...!!!")
            content = file.read()
            word_size = len(word)
            count = 0

            for i in range(len(content)):
                if content[i:i+word_size] == word:
                    count += 1

    except FileNotFoundError:
        print("Error : File Not Found")
        return -1

    return count

def main():
    file_name = input("Enter File Name : ")
    word = input("Enter Word : ")

    result = word_frequency(file_name, word)

    if result != -1:
        print(f"Frequency of {word} is : {result}")

if __name__ == "__main__":
    main()