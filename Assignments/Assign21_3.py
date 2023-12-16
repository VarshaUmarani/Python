# Accept Character from user and check whether it is digit or not (0-9). 

# Input : 7 
# Output : TRUE 

# Input : d 
# Output : FALSE

def CheckDigit(Ch):
	if Ch >= '0' and Ch <= '9':
		return True
	else:
		return False
	
def main():
	Ch = input("Enter Character : ")

	bRet = CheckDigit(Ch)

	if bRet == True:
		print("{} is Digit".format(Ch))
	else:
		print("{} is Not a Digit".format(Ch))

if __name__ == "__main__":
	main()