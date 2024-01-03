# Multi - processing

import os
import multiprocessing

def Process1():
	print("Process1 is created.!")
	print("PID of Process1 is : ",os.getpid())
	print("PID of parent process of Process1 is : ",os.getppid())

def Process2():
	print("Process2 is created.!")
	print("PID of Process2 is : ",os.getpid())
	print("PID of parent process of Process2 is : ",os.getppid())

def main():
	print("Inside main process.!")
	print("PID of main process is : ",os.getpid())
	print("PID of parent process of main is : ",os.getppid())

	process1 = multiprocessing.Process(target = Process1,args = ())
	process2 = multiprocessing.Process(target = Process2,args = ())

	process1.start()
	process2.start()

if __name__ == "__main__":
	main()