# Accept on number from user if number is less than 10 then print 
# “Hello” otherwise print “Demo”.

def DisplayPattern(No):
	if No < 10:
		print("Jay Ganesh...!!!")
	else:
		print("Jay Shree Ram...!!!")

def main():
	Num = int(input("Enter Number : "))

	DisplayPattern(Num)

if __name__ == "__main__":
	main()