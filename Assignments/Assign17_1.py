# Accept N numbers from user and return difference between summation 
# of even elements and summation of odd elements. 

# Input : N : 6 
# Elements : 85 66 3 80 93 88 
# Output : 53 (234 - 181) 

class Numbers:
    def __init__(self,Size):
        self.Size = Size
        self.Arr = []

    def Accept(self):
        print("Enter Elements into a list : ")
        for i in range(self.Size):
            self.Arr.append(int(input()))

    def Difference(self):
        OddSum = 0
        EvenSum = 0
        for i in range(self.Size):
            if self.Arr[i] % 2 == 0:
                EvenSum = EvenSum + self.Arr[i]
            else:
                OddSum = OddSum + self.Arr[i]
        return EvenSum - OddSum

def main():
    Size = int(input("Enter Number of Elements : "))

    obj = Numbers(Size)
    obj.Accept()

    Ret = obj.Difference()
    print("Difference is :",Ret)

if __name__ == "__main__":
    main()