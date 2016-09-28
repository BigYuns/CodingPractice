def bubbleSort(n): 
	for end in range(len(n)-1,0,-1): 
		for i in range(end): 
			if n[i] > n[i+1]: 
				n[i], n[i+1] = n[i+1], n[i]
	return n 

def test1(): 
 arr = [54,26,93,17,77,31,44,55,20]
 print bubbleSort(arr)


if __name__ == '__main__': 
	test1() 


"""
What is bubble sort?
Starting at index 0, swapping the neighboring element up to n-i, (where i =1 and increasing)
at each element in the array . put the larger number at the end. 
Key point: end is moving. starting is always the same. 

Pros: has the capabiltity to do something most sorting alogrithm cannot because it passes through the unsorted part of the array. : can check whhere the list is sorted  because when the exchange stops, it means after the stoppoing position, the list is sorted. 

Cons: the most inefficient sorting method 
-> exchange items before the final location is known. 

"""


