# Accept file name and one string from user and return the frequency of that string from file.
# Input : Demo.txt Marvellous 
# Search “Marvellous” in Demo.txt 

def main():
	Frequency = 0

	print("Enter File Name : ")
	Name = input()

	print("Enter String : ")
	str = input()

	fobj = open(Name,"r")

	str1 = fobj.read()

	for s in str1.split():
		if s == str:
			Frequency = Frequency + 1

	print("Frequency is :",Frequency)

if __name__ == "__main__":
	main()