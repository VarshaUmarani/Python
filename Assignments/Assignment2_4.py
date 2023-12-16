# Write a program which accept one number from user and return addition of its factors.

# Input : 12
# Output : 16   (1+2+3+4+6)

# Using For loop
def SumofFactors(Num):
	Sum = 0

	for i in range(1,int(Num/2)+1):
		if Num % i == 0:
			Sum = Sum + i

	return Sum

# Using While loop
def SumofFactorsUsingWhile(Num):
	Sum = 0
	i = 1

	while i <= int(Num/2):
		if Num % i == 0:
			Sum = Sum + i
		i = i + 1

	return Sum

def main():
	No = int(input("Enter Number : "))

	Ret = SumofFactors(No)
	print("Addition of Factors of {} is : {}".format(No,Ret))

if __name__ == "__main__":
	main()