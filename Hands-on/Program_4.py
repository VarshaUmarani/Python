# Write a Python program that calculates the area of a circle based on the radius entered by the user.

# Input  : r = 1.1
# Output : Area = 3.8013271108436504

from math import pi

def AreaofCircle(Value):
	Ans = pi * Value ** 2
	return Ans

def main():
	Radius = float(input("Enter Radius of the Circle : "))

	Area = AreaofCircle(Radius)
	print("Area of Circle is : ",Area)

if __name__ == "__main__":
	main()