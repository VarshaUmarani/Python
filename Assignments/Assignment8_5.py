# Design python application which contains two threads named as thread1 and thread2. 
# Thread1 display 1 to 50 on screen and thread2 display 50 to 1 in reverse order on 
# screen. After execution of thread1 gets completed then schedule thread2.

import threading
from time import sleep

def thread1():
	for i in range(1,51,1):
		print(i,end = "\t")
	print()

def thread2():
	for i in range(50,0,-1):
		print(i,end = "\t")
	print()

def main():
	t1 = threading.Thread(target = thread1, args = ())
	t2 = threading.Thread(target = thread2, args = ())

	t1.start()
	t2.start()

if __name__ == "__main__":
	main()