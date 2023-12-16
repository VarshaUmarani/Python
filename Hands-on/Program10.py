# Accept file name and one string from user and return the frequency of that string from file. 
# Input : Demo.txt Marvellous 
# Search “Marvellous” in Demo.txt 

def main():
	Freq = 0

	Name = input("Enter File Name : ")
	Str = input("Enter String : ")

	fobj = open(Name,"r")

	Str1 = fobj.read()
	Str1 = Str1.split()

	for s in Str1:
		if s == Str:
			Freq = Freq + 1

	print("Frequency of {} is : {}".format(Str,Freq))

if __name__ == "__main__":
	main()