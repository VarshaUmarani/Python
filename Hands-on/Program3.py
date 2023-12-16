# Write a Python program to display the current date and time.

# Sample Output :
# Current date and time :

import datetime as dt

def main():
	time = dt.datetime.now()
	print("Current Date is : ",time.strftime("%d-%m-%Y"))
	print("Current Time is : ",time.strftime("%H:%M:%S"))

if __name__ == "__main__":
	main()