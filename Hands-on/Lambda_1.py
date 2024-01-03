# Named Function
def Addition(Value1,Value2):
	return Value1 + Value2

# Anonymous or lambda Function
# Name = lambda parameters : body
Summation = lambda Value1, Value2 : Value1 + Value2

def fun(Name):
	Ret = Name(10,20)
	print("Value from fun is : ",Ret)

def main():
	No1 = int(input("Enter First Number : "))
	No2 = int(input("Enter Second Number : "))

	Ret = Addition(No1,No2)
	print("Addition is : ",Ret)

	Ret = Summation(No1,No2)
	print("Summation with lambda is : ",Ret)

	fun(Summation)
	fun(Addition)

if __name__ == "__main__":
	main()