# default arguments
# default argument order should be from right to left
def AreaofCircle(Radius,PI=3.14):
	print("Value of PI is : ",PI)
	Area = PI * (Radius **2)
	return Area

def main():
	AreaofCircle(10)
	AreaofCircle(10.25,3.15)

if __name__ == "__main__":
	main()