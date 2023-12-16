# Accept character from user. If it is capital then display all the characters from the input characters till Z. 
# If input character is small then print all the characters in reverse order till a. In other cases return directly. 

# Input : Q 
# Output : Q R S T U V W X Y Z 

# Input : m 
# Output : m l k j i h g f e d c b a 

# Input : 8 
# Output : 

def Display(ch):
	if ch >= 'A' and ch <= 'Z':
		while ch <= 'Z':
			print(ch,end = "  ")
			ch = chr(ord(ch) + 1)
	elif ch >= 'a' and ch <= 'z':
		while ch >= 'a':
			print(ch,end = "  ")
			ch = chr(ord(ch) - 1)
	else:
		pass

def main():
	ch = input("Enter Character : ")

	Display(ch)

if __name__ == "__main__":
	main()