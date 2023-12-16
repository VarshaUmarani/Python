# Accept one character from user and convert case of that character. 

# Input : a Output : A 
# Input : D Output : d

def ConvertCase(ch):
	if ch >= 'a' and ch <= 'z':
		ch = chr(ord(ch) - 32)
		print(ch)
	elif ch >= 'A' and ch <= 'Z':
		ch = chr(ord(ch) + 32)
		print(ch)
	else:
		print(ch)

def main():
	Ch = input("Enter Character : ")

	ConvertCase(Ch)

if __name__ == "__main__":
	main()