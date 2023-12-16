# In-Built function from module
def Subtraction(No1,No2):		# 100
	return No1 - No2

# Decorator
def SubDecorator(func_name):	# 200 	func_name = 100 (subtraction)
	def Updater(No1,No2):		# 300
		if No1 < No2:			# if First parameter is smaller than second
			No1,No2 = No2,No1
		return func_name(No1,No2)	# return call 100(21,11) -> subtraction(21,11) -> 10

	return Updater				# return 300

def main():						# 400
	# Sub contains 300
	Sub = SubDecorator(Subtraction)  				# Call 200(100)
	Num1 = int(input("Enter First Number : "))		# 11
	Num2 = int(input("Enter Second Number : ")) 	# 21

	Ret = Sub(Num1,Num2)				# Call 300(11,21) -> ret = Updater(Num1,Num2) -> ret = 10
	print("Subtraction is : ",Ret)		# Subtraction is : 10

if __name__ == "__main__":
	main()								# Call 400


#    Method Reference Table
#   	Function          Reference
# 	      main				400
#      SubDecorator			200
#  		 Updater			300
# 	   Subtraction			100