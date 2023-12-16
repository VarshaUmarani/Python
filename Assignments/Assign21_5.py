# Accept division of student from user and depends on the division display exam timing. 
# There are 4 divisions in school as A,B,C,D. Exam of division A at 7 AM, B at 8.30 AM, C at 9.20 AM and D at 10.30 AM. 
# (Application should be case insensitive) 

# Input : C 
# Output : Your exam at 9.20 AM 

# Input : d 
# Output : Your exam at 10.30 AM

def CheckSchedule(div):
	if div == 'A' or div == 'a':
		print("Your Exam is Scheduled at 7 A.M")
	elif div == 'B' or div == 'b':
		print("Your Exam is Scheduled at 8:30 A.M")
	elif div == 'C' or div == 'c':
		print("Your Exam is Scheduled at 9:20 A.M")
	elif div == 'D' or div == 'd':
		print("Your Exam is Scheduled at 10:30 A.M")
	else:
		print("Entered Division Doesn't Exist...!!!")

def main():
	Div = input("Enter Your Division : ")

	CheckSchedule(Div)

if __name__ == "__main__":
	main()