# Demonstration of Dictionary
# Program to create and traverse nested dictionary.

def main():
	Employee = {11 : {"Name":"Varsha","Age":22},21 : {"Name":"Vaishali","Age":24},51 : {"Name":"Niteen","Age":26}}

	print("Employee information is : ")

	for eid,information in Employee.items():
		print("Employee ID is : ",eid)
		for key in information:
			print("{} : {}".format(key,information[key]))

if __name__ == "__main__":
	main()