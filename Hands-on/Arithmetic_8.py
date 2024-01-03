# Accept two Numbers from user and perform Addition of that numbers
# Using Addition Function

# Input : 10 11
# Output : 21

# Definition of Addition Function
def Addition(value1, value2):
	ret = value1 + value2
	return ret

def main():
	No1 = int(input("Enter First Number : "))
	No2 = int(input("Enter Second Number : "))

	Ans = Addition(No1,No2)
	print("Addition is :",Ans)

if __name__ == "__main__":
	main()

# 15  16  8  9  10  12  4  5  6  13  16  (Stop)
