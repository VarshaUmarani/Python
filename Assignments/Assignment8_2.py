# Design python application which creates two threads as evenfactor and oddfactor. Both the thread 
# accept one parameter as integer. Evenfactor thread will display addition of even factors of given 
# number and oddfactor will display addition of odd factors of given number. After 
# execution of both the thread gets completed main thread should display message as “exit from main”.

import threading

def Factors(func,Value,lock):
	func(Value,lock)

def EvenFactors(Value,lock):
	lock.acquire()

	Sum = 0
	for i in range(1,int(Value/2)+1):
		if (Value % i == 0) and (i % 2 == 0):
			print(i,end = " ")
			Sum += i

	print()
	print("Addition of Even Factors is : ",Sum)

	lock.release()

def OddFactors(Value,lock):
	lock.acquire()

	Sum = 0
	for i in range(1,int(Value/2)+1):
		if (Value % i == 0) and (i % 2 != 0):
			print(i,end = " ")
			Sum += i

	print()
	print("Addition of Odd Factors is : ",Sum)

	lock.release()

def main():
	lock = threading.Lock()

	Num = int(input("Enter Number : "))
	thread1 = threading.Thread(target = Factors, args = (EvenFactors,Num,lock,))
	thread2 = threading.Thread(target = Factors, args = (OddFactors,Num,lock,))

	thread1.start()
	thread2.start()

	thread1.join()
	thread2.join()

	print("Exit from main..!!")

if __name__ == "__main__":
	main()