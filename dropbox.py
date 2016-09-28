"""
Palantir Grid Illumination Problem  + Drobpox Coding Problem 
"""
"""
Question: 
You are given a square grid. It is N by N. 
(1,1) represents the left bottom. 

Each cell can have one lamp. Since the lamp is small enough, once you put it in a cell, it illuminates through the whole direciton (vertically, horizontally, diagnoally). 
You are given a list of lamps. It is the list of coordinatino of lamps. ex: [(1,2), (3,4)]

Also you are given a list of coordination of interest positions. At the interest position, you are going to turn off all lamps that are located within the neighboring area. 
Neighboring area is defined the small square whose middle spot is the given location. 
Then, you are going to check whether the interest position is still illuminated. 


You are given like the following info: 
[N, list of lamps, list of interested positions]
Output should be: 
"Light" if the position of the interest is still illuminated, 
"Dark" If the position of the interest is not. 

ex) 
input: 
N: 8, 
List of lamps: [(1,3), (2,4), (3,5)]
List of the poisition of the interest: [[2,4], [5,7],[1,6]]

["Light", "Dark, "Light"]
"""


def gridIllumination(N,lamps,interestPos): 
	result = []
	#count = 0 
	for i in interestPos: 
		tmp = lamps
		r = lamps[i][0]
		c = lamps[i][1]
		#check the neighboring squares sround the interestPos// 
		index = interestpPos.index([r,c])
		for col in range(c-1,c+2): 
			for row in range(r-1,r+2): 
				if [col,row] in tmp: 
					tmp.remove([col,row])

		#the list of lamps is updated. 

		# for column in range(c-1, c+2): 
		# 	for row in range(r-1, r+2): 
		# 		if [c,r] not in result: 
		# 			count +=1
		traverse(c,r,result,index)
		
		# if [c,r] in result:
		# 	ind = result.index([c,r])
		# 	result[ind] = "Light"

		# if count==8: 
		# 	result.append("Dark")
		
	return result 



def traverse(c,r,result,index): 
	if [c,r] in lamps: 
		#col and row position is lit 
		result.append("Light")
		return 

	if c > N or r>N or c <1 or r <0:  
		return 

	for col in range(c-1, c+1): 
		for row in range(r-1, r+1): 
			if len(result) != len(interestPos[0:index]): 
				traverse(col,row,result,index)
				if (c!=col and r!=row): 
					return
			else
				return 


	# if result[index] != "Light": 
	# 	traverse(c-1,r-1,result)
	# if result[index] != "Light": 
	# 	traverse(c,r-1,result)
	# if result[index] != "Light": 
	# 	traverse(c+1,r-1,result)
	# if result[index] != "Light": 
	# 	traverse(c-1,r,result)
	# if result[index] != "Light": 
	# 	traverse(c+1,r,result)
	# if result[index] != "Light": 
	# 	traverse(c-1,r+1,result)
	# if result[index] != "Light": 
	# 	traverse(c,r+1,result)
	# if result[index] != "Light": 
	# 	traverse(c+1,r+1,result)
	
	result.append("Dark")
	return result 


if __name__== '__main__': 


	