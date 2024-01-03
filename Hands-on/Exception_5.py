# Program to demonstrate concept of exception handling.
# Creating user defined exceptions

# AgeInvalid class inherits Exception class
class AgeInvalid(Exception):
	def __init__(self,data):
		self.data = data

def main():
	try:
		age = int(input("Enter your age for PAN Card : "))
		if age < 18:
			raise AgeInvalid("You are not eligible for PAN Card.!")

	except AgeInvalid as obj:
		print(obj)

	else:
		print("You will get your PAN Card within 7 working days..!!")

if __name__ == "__main__":
	main()