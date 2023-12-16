# Implementation of ATM functionalities like Desposit and Withdraw 
# Using synchronisation and multithreading.

import threading

Amount = 1000

def ATM(func,lock):
	func(lock)

def Deposit(lock):
	lock.acquire()
	Value = int(input("Enter the amount to Deposit : "))
	global Amount

	Amount = Amount + Value
	print("Amount Deposited Successfully..")
	print("Balance Amount is : ",Amount)

	lock.release()

def Withdraw(lock):
	lock.acquire()
	Value = int(input("Enter the amount to Withdraw : "))
	global Amount

	if Value > Amount:
		print("There is no sufficient balance")
	else:
		Amount = Amount - Value
		print("Amount Withdraw Successfully..")
		print("Balance Amount is : ",Amount)

	lock.release()

def main():
	print("Welcome to ATM..!")

	lock = threading.Lock()

	thread1 = threading.Thread(target = ATM,args = (Deposit,lock,))
	thread2 = threading.Thread(target = ATM,args = (Withdraw,lock,))

	thread1.start()
	thread2.start()

	thread1.join()
	thread2.join()

	print("ATM application closed..!")

if __name__ == "__main__":
	main()