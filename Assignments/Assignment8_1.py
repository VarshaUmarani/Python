# Design python application which creates two thread named as even and odd. Even thread 
# will display first 10 even numbers and odd thread will display first 10 odd numbers.

import threading

def Display(func,lock):
	func(lock)

def EvenNumbers(lock):
	lock.acquire()
	print("First 10 Even Numbers are : ")
	j = 2
	for i in range(0,10):
		print(j)
		j += 2
	lock.release()

def OddNumbers(lock):
	lock.acquire()
	print("First 10 Odd Numbers are : ")
	j = 1
	for i in range(0,10):
		print(j)
		j += 2
	lock.release()

def main():
	lock = threading.Lock()

	t1 = threading.Thread(target = Display, args = (EvenNumbers,lock,))
	t2 = threading.Thread(target = Display, args = (OddNumbers,lock,))

	t1.start()
	t2.start()

if __name__ == "__main__":
	main()