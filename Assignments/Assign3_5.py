#  Accept on character from user and check whether that character is vowel 
# (a,e,i,o,u) or not.

# Input : E Output : TRUE 
# Input : d Output : FALSE

def CheckVowel(Ch):
	Ch = Ch.lower()

	if Ch == 'a' or Ch == 'e' or Ch == 'i' or Ch == 'o' or Ch == 'u':
		return True
	else:
		return False

def main():
	Ch = input("Enter Character : ")

	bRet = CheckVowel(Ch)
	if bRet == True:
		print("{} is Vowel".format(Ch))
	else:
		print("{} is Consonant".format(Ch))

if __name__ == "__main__":
	main()