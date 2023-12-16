# In-Built function from module
def Subtraction(No1,No2):		# 100
	return No1 - No2

# Decorator
def SubDecorator(func_name):	# 200 	func_name = 100
	def Updater(No1,No2):		# 300
		if No1 < No2:			# if First parameter is small
			No1,No2 = No2,No1
		return func_name(No1,No2)	# return (call 100(21,11))  -> 10

	return Updater				# return 300

# Sub contains 300
Subtraction = SubDecorator(Subtraction)  		# Call 200(100)

Num1 = int(input("Enter First Number : "))		# 11
Num2 = int(input("Enter Second Number : ")) 	# 21

Ret = Subtraction(Num1,Num2)		# Call 300(11,21) -> Ret = Updater(Num1,Num2)
print("Subtraction is :",Ret)		# Subtraction is 10


#    Method Reference Table
#   	Function          Reference
#      SubDecorator			200
#  		 Updater			300
# 	   Subtraction			100