import pandas as pd
from sklearn import tree
from sklearn import preprocessing
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

def DecisionTree(path):
	data = pd.read_csv(path)

	print("Balls Dataset loaded successfully.!!")
	print("Volume of dataset is : ",len(data))

	Weight = data.Weight
	Surface = data.Surface
	Label = data.Label

	labelobj = preprocessing.LabelEncoder()

	Weight_Encoded = labelobj.fit_transform(Weight)
	Surface_Encoded = labelobj.fit_transform(Surface)
	Target = labelobj.fit_transform(Label)

	Features = list(zip(Weight_Encoded,Surface_Encoded))

	data_train,data_test,target_train,target_test = train_test_split(Features,Target,test_size=0.5)

	obj = tree.DecisionTreeClassifier()

	obj.fit(data_train,target_train)

	Output = obj.predict(data_test)
	print("-"*170)

	for i in range(len(data_test)):
		print("ID : %d\t Expected Result : %s\t Predicted Result : %s\t" %(i,target_test[i],Output[i]))

	print("-"*170)

	Accuracy = accuracy_score(target_test,Output)
	return Accuracy

def main():
	print("-------------------------Decision Tree Algorithm for Balls Dataset-------------------------")

	name = input("Enter file name which contains dataset : ")

	Ret = DecisionTree(name)
	print("Accuracy of Decision Tree is : ",Ret*100,"%")

	print("-"*170)

if __name__ == "__main__":
	main()