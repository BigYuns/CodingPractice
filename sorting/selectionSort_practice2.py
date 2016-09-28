import sys

def findMin(arr): 
	minV = sys.maxint 
	for i in arr: 
		if minV > i:
			minV = i 
	return minV 

def selectionSort(n): 
	for i in range(len(n)): 
		minVal = findMin(n[i:len(n)])
		index = n.index(minVal)
		n[i],n[index] = minVal, n[i]

	return n     

def test1():
	arr = [53,25,13,22,9]
	print selectionSort(arr)


if __name__ == '__main__': 
	test1() 


"""
Important Key Point: 
findMin: minVlaue that I want to compare should be actually maximum. 
And once it finds the smaller one always should get updated. 

Swapping variables in python: 
	-you can just literally assign it. 
"""