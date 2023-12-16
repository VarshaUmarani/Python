# Design python application which creates two threads as evenlist and oddlist. Both the threads accept list 
# of integers as parameter. Evenlist thread add all even elements from input list and display the addition. 
# Oddlist thread add all odd elements from input list and display the addition.

import threading

def EvenList(list,lock):
	lock.acquire()
	Sum = 0
	print("Even Elements in list are : ")
	for i in range(len(list)):
		if list[i] % 2 == 0:
			print(list[i])
			Sum = Sum + list[i]

	print("Addition of Even Elements in List is :",Sum)
	lock.release()

def OddList(list,lock):
	lock.acquire()
	Sum = 0
	print("Odd Elements in list are : ")
	for i in range(len(list)):
		if list[i] % 2 != 0:
			print(list[i])
			Sum = Sum + list[i]

	print("Addition of Odd Elements in List is :",Sum)
	lock.release()

def main():
	lock = threading.Lock()

	Arr = []
	Size = int(input("Enter the Number of Elements : "))

	print("Enter Elements into the list : ")
	for i in range(Size):
		Value = int(input())
		Arr.append(Value)

	t1 = threading.Thread(target = EvenList, args = (Arr,lock,))
	t2 = threading.Thread(target = OddList, args = (Arr,lock,))

	t1.start()
	t2.start()

if __name__ == "__main__":
	main()