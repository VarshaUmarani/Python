# There is one data set of wether conditions. That dataset contains information as wether and we have to decides whether to 
# play or not. Data set contains the target variable as Play which indicates whether to play or not. 

# Consider below Play Predictor Dataset as

# According to above dataset there are two features as 
# 1.Wether 
# 2.Temperature 

# We have two labels as 
# 1.Yes 
# 2.No 

# There are three types of different entries under Wether as 
# 1.Sunny 
# 2.Overcast 
# 3.Rainy 

# There are three types of different entries under Temperature as 
# 1.Hot 
# 2.Cold 
# 3.Mild 

# We have to design Machine Learning application which uses Classification technique.

import pandas as pd
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier

def PlayPredictor(path,weather,temperature):
	# Step 1 -> load data from csv
	data = pd.read_csv(path,index_col=0)

	print("Play Predictor dataset loaded successfully.!")
	print("Volume of dataset is : ",len(data))

	# We can replace these lines by passing these values directly to fit_transform() method
	Weather = data.Weather
	Temperature = data.Temperature
	Play = data.Play

	# Step 2 -> Prepare data
	# Creating object of LabelEncoder 
	labelobj = preprocessing.LabelEncoder()

	# Converting string labels into numbers
	Weather_Encoded = labelobj.fit_transform(Weather)
	Temperature_Encoded = labelobj.fit_transform(Temperature)

	# Combining Weather and Temperature into single list of tuples
	Features = list(zip(Weather_Encoded,Temperature_Encoded))
	Target = labelobj.fit_transform(Play)

	obj = KNeighborsClassifier()

	obj.fit(Features,Target)

	Result = obj.predict([[weather,temperature]])

	if Result == 1:
		print("You can play match today.!")
	else:
		print("You cannot play match today.!")

def main():
	print("--------------------------Play Predictor Case Study-------------------------")

	name = input("Enter the name of file which contains dataset : ")

	weather = input("Enter Weather : ")
	temperature = input("Enter Temperature : ")

	if weather.lower() == "overcast":
		weather = 0
	elif weather.lower() == "rainy":
		weather = 1
	elif weather.lower() == "sunny":
		weather = 2
	else:
		print("Error : Invalid input for Weather.!")

	if temperature.lower() == "cool":
		temperature = 0
	elif temperature.lower() == "hot":
		temperature = 1
	elif temperature.lower() == "mild":
		temperature = 2
	else:
		print("Error : Invalid input for Temperature.!")

	PlayPredictor(name,weather,temperature)

if __name__ == "__main__":
	main()