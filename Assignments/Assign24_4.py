# Write a program which accept string from user and display only digits from that string. 

# Input : “marve89llous121” 
# Output : 89121 

# Input : “Demo” 
# Output :

def Count_Digits(str):
	Cnt = 0
	for c in str:
		if c >= '0' and c <= '9':
			Cnt = Cnt + 1
	return Cnt

def main():
	Str = input("Enter String : ")

	Ret = Count_Digits(Str)
	print("Count of Digits is :",Ret)

if __name__ == "__main__":
	main()