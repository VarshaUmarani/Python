# Write a recursive program which display below pattern.

# Input : 5 
# Output : * * * * * 

def Display_Pattern(Num):
	if Num != 0:
		print("*",end="\t")
		Display_Pattern(Num-1)

def main():
	No = int(input("Enter Number : "))

	Display_Pattern(No)

if __name__ == "__main__":
	main()