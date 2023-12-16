import numpy as np
import pandas as pd
from sklearn import preprocessing
from scipy.spatial import distance
from sklearn.model_selection import train_test_split

class KNN:
	@classmethod
	def CalculateDistance(cls,X,Y):
		return distance.euclidean(X,Y)

	def fit(self,data_train,data_test):
		self.data_train = data_train
		self.data_test = data_test

	def predict(self,data_target):
		Predictions = []

		for row in data_target:
			target = self.ShortestDistance(row)
			Predictions.append(target)

		return Predictions

	def ShortestDistance(self,row):
		MinIndex = 0
		MinDistance = KNN.CalculateDistance(row,self.data_train[0])

		for i in range(1,len(self.data_train)):
			Distance = KNN.CalculateDistance(row,self.data_train[i])
			if Distance < MinDistance:
				MinIndex = i
				MinDistance = Distance

		return self.data_test[MinIndex]

def CalculateAccuracy(expected_result,actual_result):
	total = len(expected_result)
	actual = 0

	for i in range(len(expected_result)):
		if actual_result[i] == expected_result[i]:
			actual += 1

	print("Number of Wrong Predictions is : ",(total-actual))
	print("-"*170)

	Accuracy = (actual / total) * 100
	return Accuracy

def PlayPredictor(path):
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

	# Splitting training and testing data
	data_train,data_test,target_train,target_test = train_test_split(Features,Target,test_size=0.5)

	obj = KNN()

	# Step 3 -> Train the model using training sets
	obj.fit(data_train,target_train)

	# Step 4 -> Test model
	output = obj.predict(data_test)

	print("-"*170)

	for i in range(len(output)):
		print("ID : %d\t Expected Result : %s\t Predicted Result : %s\t" %(i,target_test[i],output[i]))

	print("-"*170)

	# Calculate accuracy of machine learning model
	Accuracy = CalculateAccuracy(target_test,output)
	return Accuracy

def main():
	print("-------------------------User defined KNN implementation for Play Predictor dataset-------------------------")

	file_name = input("Enter the name of file which contains play predictor dataset : ")

	ret = PlayPredictor(file_name)
	print("Accuracy of User Defined KNN Algorithm is : ",ret,"%")

	print("-"*170)

if __name__ == "__main__":
	main()