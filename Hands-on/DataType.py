def main():
	a = 11
	print("Value of a is : ",a)					#11
	print("Data type of a is : ",type(a))		# <class 'int'>
	print("Unique ID of a is : ",id(a))			# It is used to display the unique ID of the object (Address)

	b = 12.45
	print("Value of b is : ",b)
	print("Data type of b is : ",type(b))
	print("Unique ID of b is : ",id(b))

	c = 4 + 3j
	print("Value of c is : ",c)
	print("Data type of c is : ",type(c))
	print("Unique ID of c is : ",id(c))

	d = "Jay Ganesh"
	print("Value of d is : ",d)
	print("Data type of d is : ",type(d))
	print("Unique ID of d is : ",id(d))

	e = True
	print("Value of e is : ",e)
	print("Data type of e is : ",type(e))
	print("Unique ID of e is : ",id(e))

	f = [10,20,30,40]
	print("Value of f is : ",f)
	print("Data type of f is : ",type(f))

	g = {10,20,30,40,50}
	print("Value of g is : ",g)
	print("Data type of g is : ",type(g))

	h = (10,20,30,40)
	print("Value of h is : ",h)
	print("Data type of h is : ",type(h))

	i = {"a":10,"b":20,"c":30,"d":40}
	print("Value of i is : ",i)
	print("Data type of i is : ",type(i))

	j = None
	print("Value of j is : ",j)
	print("Data type of j is : ",type(j))

if __name__ == "__main__":
	main()