# Iterative Method using for loop
def IterativeFor(No):
	print("Calling Iterative Function with for loop")
	for i in range(No):
		print("Hello World.!")

# Iterative Method using while loop
def IterativeWhile(No):
	print("Calling Iterative Function with while loop")
	while No != 0:
		print("Jay Ganesh.!")
		No = No - 1

# Calling the function from the same function itself
def Recursive(No):
	if No != 0:
		print("Jay Shree Ram.!")
		No = No -1
		Recursive(No)
		# Recursive(No-1)

def main():
	Value = int(input("Enter Number of Iterations : "))

	IterativeFor(Value)
	IterativeWhile(Value)

	print("Calling Recursive Function")
	Recursive(Value)

if __name__ == "__main__":
	main()