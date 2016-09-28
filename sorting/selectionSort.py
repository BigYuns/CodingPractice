"""
Selection Sort: 
Time Complexity: O(n^2)
How it works: 
Selects the smallest element of the array and places it at index 0, then selects the second smallest and places it in index 1, 
then third smallest in index 2, etc. 


"""
import sys

def findMin(arr): 
	smallest = sys.maxint 
	for i in arr: 
		if i < smallest: 
			smallest = i 

	return smallest

def selectionSort(n): 
	#select the smallest element 
	#swap it with the first elemetn. 
	for i in range(len(n)):
		tmp = n[i] 
		minVal = findMin(n[i:len(n)])
		index = n.index(minVal)
		n[index] = tmp 
		n[i]  = minVal

	return n 

def test1():
	arr = [53,25,13,22,9]
	print selectionSort(arr)


if __name__ == '__main__': 
	test1() 


 

