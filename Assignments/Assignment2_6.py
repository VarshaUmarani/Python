# Write a program which accept one number and display below pattern.

# Input : 5
# Output :	*	*	*	*	*
#			*	*	*	*
# 			*	*	*
#			*	*
#			*

def Display_Pattern(Num):
	j = 0
	for i in range(Num,0,-1):
		for j in range(i):
			if j <= i:
				print("*",end="\t")
		print()

def main():
	No = int(input("Enter Number : "))

	Display_Pattern(No)

if __name__ == "__main__":
	main()