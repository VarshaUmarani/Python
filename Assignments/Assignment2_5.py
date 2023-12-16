# Write a program which accept one number from user and check whether number is prime or not.

# Input : 5
# Output : It is Prime Number

def Check_Prime(Num):
	Flag = 0
	for i in range(2,int(Num/2)+1):
		if Num % i == 0:
			Flag = 1
			break

	if Flag == 0:
		return True
	else:
		return False

def main():
	No = int(input("Enter Number to Check Prime or not : "))

	Ret = Check_Prime(No)
	if Ret == True:
		print("{} is Prime Number.!".format(No))
	else:
		print("{} is not a Prime Number.!".format(No))

if __name__ == "__main__":
	main()