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

def PlayPredictor():
	data = pd.read_csv("PlayPredictor.csv")

	print("Play Predictor dataset loaded successfully.!")
	print("Volume of dataset is : ",len(data))

	Weather = data.Weather
	Temperature = data.Temperature
	Play = data.Play

	labelobj = preprocessing.LabelEncoder()

	Weather_Encoded = labelobj.fit_transform(Weather)
	Temperature_Encoded = labelobj.fit_transform(Temperature)
	Target = labelobj.fit_transform(Play)

	Features = list(zip(Weather_Encoded,Temperature_Encoded))

	obj = KNeighborsClassifier()

	obj.fit(Features,Target)

	Result = obj.predict([[0,2]])

	if Result == 1:
		print("You can play match today.!")
	else:
		print("You cannot play match today.!")

def main():
	print("--------------------------Play Predictor Case Study-------------------------")

	PlayPredictor()

if __name__ == "__main__":
	main()