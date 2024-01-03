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

	# finally block
	finally:
		# Deallocating the resource is expected
		del no1
		del no2
		print("Deallocate all the resources.!")

if __name__ == "__main__":
	main()