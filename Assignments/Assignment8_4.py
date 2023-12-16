# Design python application which creates three threads as small, capital, digits. All the threads accepts string
# as parameter. Small thread display number of small characters, capital thread display number of capital 
# characters and digits thread display number of digits. Display id and name of each thread.

import threading
import os

def Small(string,lock):
	lock.acquire()

	Sum = 0

	print("Id of the Current thread is :",os.getpid())

	print("Small characters from String are : ")
	for i in string:
		if i >= 'a' and i <= 'z':
			Sum += 1
			print(i)

	print("Number of Small characters is : ",Sum)
	lock.release()

def Capital(string,lock):
	lock.acquire()

	Sum = 0

	print("Id of the Current thread is :",os.getpid())

	print("Capital characters from String are : ")
	for i in string:
		if i >= 'A' and i <= 'Z':
			Sum += 1
			print(i)

	print("Number of Capital characters is : ",Sum)
	lock.release()

def Digits(string,lock):
	lock.acquire()

	Sum = 0

	print("Digits in string are : ")
	for i in string:
		if i >= '0' and i <= '9':
			Sum += 1
			print(i)

	print("Number of Digits is : ",Sum)
	lock.release()

def main():
	lock = threading.Lock()

	print("Enter String : ")
	str = input()

	t1 = threading.Thread(target = Capital, args = (str,lock,))
	t2 = threading.Thread(target = Small, args = (str,lock,))
	t3 = threading.Thread(target = Digits, args = (str,lock,))

	t1.start()
	t2.start()
	t3.start()

if __name__ == "__main__":
	main()