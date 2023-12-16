# CheckPrime function checks whether the number is prime or not.

def CheckPrime(Num):
	flag = 0

	for i in range(2,int(Num/2)+1):
		if Num % i == 0:
			flag = 1
			break

	if flag != 1:
		return True
	else:
		return False