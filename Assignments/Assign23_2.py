# Write a program which accept string from user and count number of small characters. 

# Input : “Marvellous” 
# Output : 9 

def Count_Small(str):
	Cnt = 0
	for s in str:
		if s >= 'a' and s <= 'z':
			Cnt = Cnt + 1
	return Cnt

def main():
	Str = input("Enter String : ")

	Ret = Count_Small(Str)
	print("Count of Small Characters is :",Ret)

if __name__ == "__main__":
	main()