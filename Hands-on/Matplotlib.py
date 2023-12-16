import pandas as pd
import matplotlib.pyplot as plt

def Display_Graph(name):
	excel_file = name
	data = pd.read_excel(name)

	print("All data from excel file")
	print(data)

	# We can pass any number as a parameter to head() function
	# If we don't pass any parameter to head() function then it displays only 5 rows
	print("First 5 rows from file")
	print(data.head())

	print("First 4 rows from file")
	print(data.head(4))

	print("Last 5 rows from file")
	print(data.tail())

	print("Last 4 rows from file")
	print(data.tail(4))

	print(data.shape)

	Sorted_data = data.sort_values(['Name'],ascending=False)

	print("Sorted data")
	print(Sorted_data)

	data['Age'].plot(kind="hist")
	plt.show()

	data['Age'].plot(kind="barh")
	plt.show()

def main():
	name = 'StudentInfo.xlsx'

	Display_Graph(name)

if __name__ == "__main__":
	main()