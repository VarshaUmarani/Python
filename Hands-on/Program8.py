def EliminatedPersons(N,K):
	if K % 2 != 0:
		print(0)
	else:
		for i in range(1,N+1):
			if i % K == 0:
				print(i,end = " ")

def main():
	S = input().split()
	X = int(S[0])
	Y = int(S[1])
	EliminatedPersons(X,Y)

if __name__ == "__main__":
	main()