from sklearn import tree

def main():
	# Step 1 & 2
	Features = [[35,"Rough"],[47,"Rough"],[90,"Smooth"],[48,"Rough"],[90,"Smooth"],
			    [35,"Rough"],[92,"Smooth"],[35,"Rough"],[35,"Rough"],[35,"Rough"],
			 	[96,"Smooth"],[43,"Rough"],[110,"Smooth"],[35,"Rough"],[95,"Smooth"]]

	Labels = ["Tennis","Tennis","Cricket","Tennis","Cricket",
			  "Tennis","Cricket","Tennis","Tennis","Tennis",
			  "Cricket","Tennis","Cricket","Tennis","Cricket"]		 	

	# Step 3
	dobj = tree.DecisionTreeClassifier()

	# Step 4
	dobj.fit(Features,Labels)

	# Step 5
	result = dobj.predict([[40,"Rough"]])

	print("Ball is : ",result)		# ValueError: could not convert string to float: 'Rough'

if __name__ == "__main__":
	main()