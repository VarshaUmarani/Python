# Write a program which accept string from user and return difference between frequency of small characters
# and frequency of capital characters. 

# Input : “MarvellouS” 
# Output : 6 (8-2)

def Difference_Count(str):
	Cnt1, Cnt2 = 0,0
	for c in str:
		if c >= 'A' and c <= 'Z':
			Cnt1 = Cnt1 + 1
		elif c >= 'a' and c <= 'z':
			Cnt2 = Cnt2 + 1
	return Cnt2 - Cnt1

def main():
	Str = input("Enter String : ")
	
	Ret = Difference_Count(Str)
	print("Difference of Count is :",Ret)

if __name__ == "__main__":
	main()