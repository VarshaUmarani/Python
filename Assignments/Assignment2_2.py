# Write a program which accept one number and display below pattern.

# Input : 5
# Output :	*	* 	*	*	*
# 			*	*	*	*	*
#			*	*	*	*	*
# 			*	*	*	*	*
#			*	*	*	*	*

def Display_Pattern(Num):
	for i in range(Num):
		for j in range(Num):
			print("*",end="\t")
		print()

def main():
	No = int(input("Enter Number : "))

	Display_Pattern(No)

if __name__ == "__main__":
	main()