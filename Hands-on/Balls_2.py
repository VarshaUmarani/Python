from sklearn import tree

# Rough - 1
# Smooth - 0

# Tennis - 1
# Cricket - 2

def main():
	# Step 1 & 2 - Convert alpha numeric input to numeric input
	#Features = [[35,"Rough"],[47,"Rough"],[90,"Smooth"],[48,"Rough"],[90,"Smooth"],
	#		    [35,"Rough"],[92,"Smooth"],[35,"Rough"],[35,"Rough"],[35,"Rough"],
	#		 	[96,"Smooth"],[43,"Rough"],[110,"Smooth"],[35,"Rough"],[95,"Smooth"]]

	Features = [[35,1],[47,1],[90,0],[48,1],[90,0],
			    [35,1],[92,0],[35,1],[35,1],[35,1],
			 	[96,0],[43,1],[110,0],[35,1],[95,0]]

	#Labels = ["Tennis","Tennis","Cricket","Tennis","Cricket",
	#		  "Tennis","Cricket","Tennis","Tennis","Tennis",
	#		  "Cricket","Tennis","Cricket","Tennis","Cricket"]		 	

	Labels = [1,1,2,1,2,1,2,1,1,1,2,1,2,1,2]

	# Step 3
	dobj = tree.DecisionTreeClassifier()

	# Step 4
	dobj.fit(Features,Labels)

	# Step 5
	result = dobj.predict([[40,1]])

	if result == 1:
		print("Your object looks like Tennis Ball")
	else:
		print("Your object looks like Cricket Ball")

if __name__ == "__main__":
	main()