# Write a program which displays ASCII table. Table contains symbol, Decimal, Hexadecimal and Octal 
# representation of every member from 0 to 255.

def main():
	for i in enumerate(range(0,256)):
		print(chr(i[1]), i[1], hex(i[1]), end=" ")
		if i[0] % 5 == 0:
			print()

if __name__ == "__main__":
	main()