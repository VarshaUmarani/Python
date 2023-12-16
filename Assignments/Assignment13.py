# Algorithm : Linear Regression
# DataSet : Advertising Dataset
# Features : TV, Radio, Television, 
# Labels : -
# Training Dataset : 70% of 200 Entries
# Testing Dataset : 30% of 200 Entries

import numpy as np
import pandas as pd

def Advertising_LinearRegression():

	# Load data
	advertising_data = pd.read_csv("Advertising.csv")
	print("Advertising Dataset loaded Successfully.!!")
	print("Size of dataset is : ",advertising_data.shape)

	# Step 2 -> Prepare data
	features = ["TV", "Radio", "NewsPaper"]

	TV = advertising_data.TV
	Radio = advertising_data.Radio
	Newspaper = advertising_data.Newspaper

	# Combining All the features into single list of tuples
	X = list(zip(TV,Radio,Newspaper))
	Y = advertising_data.Sales

	print("Length of X : ",len(X))
	print("Length of Y : ",len(Y))

	X_Mean = np.mean(X)
	Y_Mean = np.mean(Y)

	print("Mean of Independent Variable is : ",X_Mean)
	print("Mean of Dependent Variable is : ",Y_Mean)

	Numerator = 0
	Denominator = 0

	# m = (Sum(X-X_Mean) * Sum(Y-Y_Mean)) / Sum(X-X_Mean)**2
	for i in range(len(X)):
		Numerator = Numerator + ((X[i] - X_Mean) * (Y[i] - Y_Mean))
		Denominator = Denominator + ((X[i] - X_Mean)**2)

	m = Numerator / Denominator

	# Equation of line is y = mx + c
	# y = mx + c
	c = Y_Mean - (m * X_Mean)

	print("Slope (m) of Regression line is : ",m)			
	print("Y-intercept (c) of Regression line is : ",c)		

	# Findout goodness of fit i.e R Square
	Numerator = 0
	Denominator = 0
	
	# RSquare = ((m * (X[i] + c) - (Y_mean))**2) / ((Y[i] - Y_Mean)**2)
	for i in range(len(X)):
		Y_pred = m * X[i] + c
		Numerator = Numerator + (Y[i] - Y_Mean)**2
		Denominator = Denominator + (Y[i] - Y_pred)**2

	# RSquare = Numerator / Denominator
	Goodness_of_fit = 1 - (Denominator / Numerator)
	print("Goodness of fit using RSquare Method is : ",Goodness_of_fit)


def main():
	print("-------------------------Advertising dataset using Linear Regression-------------------------")

	Advertising_LinearRegression()

if __name__ == "__main__":
	main()