import os
import threading
from time import sleep

def Thread1(no):
	print("Thread1 is created.!")
	print("PID of Thread1 is : ",os.getpid())

	for i in range(no):
		sleep(1)
		print("Thread-1 : ",i)

def Thread2(no):
	print("Thread2 is created.!")
	print("PID of Thread2 is : ",os.getpid())

	for i in range(no):
		sleep(1)
		print("Thread-2 : ",i)

def main():
	print("Inside main thread.!")
	print("PID of main process is : ",os.getpid())
	print("PID of parent process of main is : ",os.getppid())

	value = 21

	# args is tuple
	thread1 = threading.Thread(target = Thread1,args = (value,))
	thread2 = threading.Thread(target = Thread2,args = (value,))

	thread1.start()
	thread2.start()

	thread1.join()
	thread2.join()

	print("End of main thread.!")

if __name__ == "__main__":
	main()