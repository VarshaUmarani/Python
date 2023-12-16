# Write a program which accept string from user and count number of capital characters. 

# Input : “Marvellous Multi OS” 
# Output : 4 

def Count_Capitals(Str):
	Cnt = 0
	for s in Str:
		if s >= 'A' and s <= 'Z':
			Cnt = Cnt + 1
	return Cnt

def main():
	Str = input("Enter String : ")

	Ret = Count_Capitals(Str)
	print("Count of Capital Characters is :",Ret)

if __name__ == "__main__":
	main()