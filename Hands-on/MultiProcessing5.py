import os
import multiprocessing

def Process1(no):
	print("Process1 is created.!")
	print("PID of Process1 is : ",os.getpid())
	print("PID of parent process of Process1 is : ",os.getppid())

	for i in range(no):
		print("Process-1 : ",i)

def Process2(no):
	print("Process2 is created.!")
	print("PID of Process2 is : ",os.getpid())
	print("PID of parent process of Process2 is : ",os.getppid())

	for i in range(no):
		print("Process-2 : ",i)

def main():
	print("Inside main process.!")
	print("PID of main process is : ",os.getpid())
	print("PID of parent process of main is : ",os.getppid())

	value = 100

	# args is tuple and , is compulsory at the end of the tuple
	process1 = multiprocessing.Process(target = Process1,args = (value,))
	process2 = multiprocessing.Process(target = Process2,args = (value,))

	process1.start()
	process2.start()

	process1.join()
	process2.join()

	print("End of main process.!")

if __name__ == "__main__":
	main()