# Keyword Arguments
def ComputerData(RAM,Processor,SSD):
	print("RAM Size is : ",RAM)
	print("Processor is : ",Processor)
	print("Size of SSD is : ",SSD)

def main():
	ComputerData(RAM=16,SSD="512 GB",Processor="i5")
	ComputerData(Processor="i7",RAM=8,SSD="256 GB")

if __name__ == "__main__":
	main()