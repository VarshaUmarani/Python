# Accept one character from user and convert case of that character. 

# Input : a Output : A 
# Input : D Output : d

def ConvertCase(ch):
	if ch >= 'a' and ch <= 'z':
		ch = ch.upper()
		print(ch)
	elif ch >= 'A' and ch <= 'Z':
		ch = ch.lower()
		print(ch)
	else:
		print(ch)

def main():
	Ch = input("Enter Character : ")

	ConvertCase(Ch)

if __name__ == "__main__":
	main()