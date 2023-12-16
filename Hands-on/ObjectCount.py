class Demo:
	Count = 0

	def __init__(self):
		Demo.Count = Demo.Count + 1

def main():
	Obj1 = Demo()
	Obj2 = Demo()

	print("Number of Objects Created is :",Demo.Count)

if __name__ == "__main__":
	main()