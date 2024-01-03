# Implementation of ATM functionalities like Desposit and Withdraw 
# Using regular approach

Amount = 1000

def ATM(func):
	func()

def Deposit():
	Value = int(input("Enter the amount to Deposit : "))
	global Amount
	Amount = Amount + Value
	print("Amount Deposited Successfully..")
	print("Balance Amount is : ",Amount)

def Withdraw():
	Value = int(input("Enter the amount to Withdraw : "))
	global Amount
	if Value > Amount:
		print("There is no sufficient balance")
	else:
		Amount = Amount - Value
		print("Amount Withdraw Successfully..")
		print("Balance Amount is : ",Amount)

def main():
	ATM(Deposit)
	ATM(Withdraw)

if __name__ == "__main__":
	main()