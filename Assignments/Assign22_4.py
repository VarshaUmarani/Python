# Accept Character from user and check whether it is special symbol or not (!, @, #, $, %, ^, &, *). 

# Input : % 
# Output : TRUE 

# Input : d 
# Output : FALSE 

def SpecialCase(ch):
	if (ch >= chr(33) and ch <= chr(47)) or (ch >= chr(58) and ch <= chr(64)):
		return True
	else:
		return False

def main():
	ch = input("Enter Character : ")

	bRet = SpecialCase(ch)
	if bRet == True:
		print("TRUE")
	else:
		print("FALSE")

if __name__ == "__main__":
	main()