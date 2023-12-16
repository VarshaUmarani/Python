# This Function will be recursively called 1000 times According to Python
# In Python, Function is also considered as object

i = 1

def Recursion():
	global i
	print(i)
	i = i + 1
	Recursion()

def main():
	Recursion()

if __name__ == "__main__":
	main()