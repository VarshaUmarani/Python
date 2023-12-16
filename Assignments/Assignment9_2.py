# Write a program which accept file name from user and open that file and display the contents of that file on screen. 
# Input : Demo.txt 
# Display contents of Demo.txt on console.

def main():
	file_name = input("Enter File Name : ")

	fobj = open(file_name,"r")

	print("Content of {} is : ".format(file_name))
	print(fobj.read())

if __name__ == "__main__":
	main()