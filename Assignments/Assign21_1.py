# Accept Character from user and check whether it is alphabet or not (A-Z a-z). 

# Input : F 
# Output : TRUE 

# Input : & 
# Output : FALSE

def CheckAlphabet(Ch):
	List1 = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
	'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	
	List2 = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
	'n','o','p','q','r','s','t','u','v','w','x','y','z']

	if Ch in List1 or Ch in List2:
		return True
	else:
		return False

def main():
	Ch = input("Enter Character : ")

	bRet = CheckAlphabet(Ch)

	if bRet == True:
		print("{} is an Alphabet".format(Ch))
	else:
		print("{} is Not an Alphabet".format(Ch))

if __name__ == "__main__":
	main()