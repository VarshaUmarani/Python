# Accept Character from user and check whether it is capital or not (A-Z). 

# Input : F 
# Output : TRUE 

# Input : d 
# Output : FALSE 

def CheckCapital(Ch):
	if chr(ord(Ch)) >= 'A' and chr(ord(Ch)) <= 'Z':
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