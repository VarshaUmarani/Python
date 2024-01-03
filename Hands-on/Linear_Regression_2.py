import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def Linear_Regression():

	# Load data
	X = [1,2,3,4,5]
	Y = [3,4,2,4,5]

	print("Value of Independent Variables X : ",X)
	print("Value of Dependent Variables Y : ",Y)

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

	print("Slope of Regression line is : ",m)			# 0.4
	print("Y-intercept of Regression line is : ",c)		# 2.4

	# Display plotting of above points
	x = np.linspace(1,6,len(X))

	y = m * x + c

	plt.plot(x,y,color='Green',label='Regression Line')
	plt.scatter(X,Y,color='Red',label='Scatter Plot')

	plt.xlabel('X - Independent Variable')
	plt.ylabel('Y - Dependent Variable')

	plt.legend()
	plt.show()

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
	print("--------------------------Linear Regression-------------------------")

	Linear_Regression()

if __name__ == "__main__":
	main()