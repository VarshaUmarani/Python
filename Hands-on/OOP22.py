class Maths:
	def __init__(self,no1,no2):
		self.no1 = no1
		self.no2 = no2

	def Add(self):
		return self.no1 + self.no2

def main():
	print("Enter First Number : ")
	x = int(input())

	print("Enter Second Number : ")
	y = int(input())

	obj = Maths(x,y)
	ret = obj.Add()
	print("Addition is :",ret)

if __name__ == '__main__':
	main()