# Accept character from user. If character is small display its corresponding capital character, 
# and if it small then display its corresponding capital. In other cases display as it is. 

# Input : Q 
# Output : q 

# Input : m 
# Output : M 

# Input : 4 
# Output : 4 
 
# Input : % 
# Output : % 

def DisplayChar(Ch):
	if Ch >= 'A' and Ch <= 'Z':
		Ch = chr(ord(Ch) + 32)
		print(Ch)
	elif Ch >= 'a' and Ch <= 'z':
		Ch = chr(ord(Ch) - 32)
		print(Ch)
	else:
		print(Ch)

def main():
	ch = input("Enter Character : ")

	DisplayChar(ch)

if __name__ == "__main__":
	main()