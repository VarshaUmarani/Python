# Write a recursive program which display below pattern. 
# Input : 5 
# Output : 1 2 3 4 5

i = 1

def Display_Pattern(Num):
	global i
	if i <= Num:
		print(i,end="\t")
		i = i + 1
		Display_Pattern(Num) 

def main():
	No = int(input("Enter Number : "))

	Display_Pattern(No)

if __name__ == "__main__":
	main()