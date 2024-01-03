# Program to demonstrate concept of exception handling.

def main():
	no1 = int(input("Enter first number : "))
	no2 = int(input("Enter second number : "))

	try:
		ans = no1 / no2
		
	except ZeroDivisionError as obj:
		print("Exception : ",obj)
	
	# Generic block
	except Exception as eobj:
		print("Exception occured : ",eobj)

	else:
		print("Division is : ",ans)

if __name__ == "__main__":
	main()