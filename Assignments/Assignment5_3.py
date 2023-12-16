# Write a recursive program which display below pattern. 
# Input : 5 
# Output : 5 4 3 2 1

def Display_Pattern(Num):
	if Num != 0:
		print(Num,end="\t")
		Num = Num - 1
		Display_Pattern(Num)

def main():
	No = int(input("Enter Number : "))

	Display_Pattern(No)

if __name__ == "__main__":
	main()