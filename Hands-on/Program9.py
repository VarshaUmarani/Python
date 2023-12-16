def main():
	Cnt = 0
	print("Enter String : ")
	str = input()

	str = str.lower()

	for s in str:
		if s == 'a' or s == 'e' or s == 'i' or s == 'o' or s == 'u':
			Cnt = Cnt + 1

	print(Cnt)

if __name__ == "__main__":
	main()