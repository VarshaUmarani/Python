# Write a program which contains one class named as BankAccount. 
# BankAccount class contains two instance variables as Name & Amount. 
# That class contains one class variable as ROI which is initialise to 10.5. 
# Inside init method initialise all name and amount variables by accepting the values from user. 
# There are Four instance methods inside class as Display(), Deposit(), Withdraw(), 
# CalculateInterest(). 
# Deposit() method will accept the amount from user and add that value in class instance variable Amount. 
# Withdraw() method will accept amount to be withdrawn from user and subtract that amount 
# from class instance variable Amount. 
# CalculateInterest() method calculate the interest based on Amount by considering rate of interest 
# which is Class variable as ROI. 
# And Display() method will display value of all the instance variables as Name and Amount. 
# After designing the above class call all instance methods by creating multiple objects.

class BankAccount:
	ROI = 10.5

	def __init__(self,Name,Amount):
		self.Name = Name
		self.Amount = Amount
		self.Interest = 1

	def Deposit(self):
		Amount = int(input("Enter the Amount to Deposit : "))
		self.Amount = self.Amount + Amount

	def Withdraw(self):
		Amount = int(input("Enter the Amount to Withdraw : "))
		self.Amount = self.Amount - Amount

	def CalculateInterest(self):
		self.Interest = (self.Amount * BankAccount.ROI)/100

	def Display(self):
		print("Name of the User is : ",self.Name)
		print("Amount in the BankAccount is : ",self.Amount)
		print("Interest Amount is : ",self.Interest)

def main():
	Name = input("Enter the Name of User : ")
	Amount = int(input("Enter the Amount : "))

	Obj = BankAccount(Name,Amount)

	Obj.Deposit()
	Obj.Withdraw()
	Obj.CalculateInterest()
	Obj.Display()

if __name__ == "__main__":
	main()