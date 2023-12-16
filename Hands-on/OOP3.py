class Arithmetic:
	def __init__(self):
		print("Inside Constructor.!")

def main():
	# Arithmetic() -> It is internally considered as Arithmetic(obj)
	# Arithmetic(obj) -> Is further internally considered as __init__(obj)
	obj = Arithmetic()

if __name__ == "__main__":
	main()