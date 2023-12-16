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
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

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
	data_train,data_test,target_train,target_test = train_test_split(Features,Target,test_size=0.3)

	obj = KNeighborsClassifier()

	# Step 3 -> Train the model using training sets
	obj.fit(data_train,target_train)

	# Step 4 -> Test model
	output = obj.predict(data_test)

	print("-"*170)

	for i in range(len(output)):
		print("ID : %d\t Expected Result : %s\t Predicted Result : %s\t" %(i,target_test[i],output[i]))

	print("-"*170)

	# Calculate accuracy of machine learning model
	Accuracy = accuracy_score(target_test,output)
	return Accuracy

def main():
	print("-------------------------User defined KNN implementation for Play Predictor dataset-------------------------")

	file_name = input("Enter the name of file which contains play predictor dataset : ")

	ret = PlayPredictor(file_name)
	print("Accuracy of User Defined KNN Algorithm is : ",ret*100,"%")

	print("-"*170)

if __name__ == "__main__":
	main()