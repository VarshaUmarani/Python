# Accept Character from user and check whether it is capital or not (A-Z). 

# Input : F 
# Output : TRUE 

# Input : d 
# Output : FALSE 

def CheckCapital(Ch):
	List1 = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
	'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

	if Ch in List1:
		return True
	else:
		return False

def main():
	Ch = input("Enter Character : ")

	bRet = CheckCapital(Ch)

	if bRet == True:
		print("{} is Capital Alphabet".format(Ch))
	else:
		print("{} is Not Capital Alphabet".format(Ch))

if __name__ == "__main__":
	main()