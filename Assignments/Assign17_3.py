# Accept N numbers from user and display all such elements which are even and divisible by 5. 

# Input : N : 6 
# Elements : 85 66 3 80 93 88 
# Output : 80

class Numbers:
    def __init__(self,Size):
        self.Size = Size
        self.Arr = []

    def Accept(self):
        print("Enter Elements into a list : ")
        for i in range(self.Size):
            self.Arr.append(int(input()))

    def Display(self):
        for i in range(self.Size):
            if self.Arr[i] % 5 == 0 and self.Arr[i] % 2 == 0:
                print(self.Arr[i],end= "  ")

def main():
    Size = int(input("Enter Number of Elements : "))

    obj = Numbers(Size)
    obj.Accept()
    obj.Display()

if __name__ == "__main__":
    main()