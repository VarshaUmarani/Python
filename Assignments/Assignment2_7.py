# Write a program which accept one number and display below pattern.

# Input : 5 
# Output : 	1 2 3 4 5 
# 			1 2 3 4 5
# 			1 2 3 4 5
#			1 2 3 4 5 
# 			1 2 3 4 5

def Display_Pattern(Num):
	for i in range(Num):
		for j in range(1,Num+1):
			print(j,end="\t")
		print()

def main():
	No = int(input("Enter Number : "))

	Display_Pattern(No)

if __name__ == "__main__":
	main()