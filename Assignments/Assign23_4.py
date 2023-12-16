# Write a program which accept string from user and check whether it contains vowels in it or not. 

# Input : “marvellous” 
# Output : TRUE 

# Input : “Demo” 
# Output : TRUE 

# Input : “xyz” 
# Output : FALSE

def Check_Vowels(str):
	flag = 0
	str = str.lower()
	for s in str:
		if s == 'a' or s == 'e' or s == 'i' or s == 'e' or s == 'u':
			flag = 1
			break
	if flag != 0:
		return True
	else:
		return False

def main():
	Str = input("Enter String : ")

	bRet = Check_Vowels(Str)
	if bRet == True:
		print("%s Contains Vowels in it...!!!"%(Str))
	else:
		print("%s Doesn't Contains Vowels in it...!!!"%(Str))

if __name__ == "__main__":
	main()