class Snakes:
	def __init__(self,arr):
		self.arr = arr
		self.Min = 0
		self.Max = 0

	def NoofHeads(self):
		self.Max = self.arr[0]
		self.Min = self.arr[0]

		for i in range(len(self.arr)):
			if self.arr[i] > self.Max:
				self.Max = self.arr[i]

		for i in range(len(self.arr)):
			if self.arr[i] < self.Min:
				self.Min = self.arr[i]

		Ret = self.Max + self.Min
		return Ret

	def ProductofHeads(self):
		Ret = self.Max * self.Min
		return Ret

def main():
	N = int(input())
	arr = []

	for i in range(N):
		arr.append(int(input()))

	obj = Snakes(arr)

	Ret1 = obj.NoofHeads()
	print(Ret1)

	Ret2 = obj.ProductofHeads()
	print(Ret2)

if __name__ == "__main__":
	main()