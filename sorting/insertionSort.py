def insertionSort(n): 
	for i in range(len(n)): 
		for j in range(i,0,-1): 
			if n[j-1] > n[j]: 
				n[j-1], n[j] = n[j], n[j-1]

	return n 


def test1(): 
 arr = [54,26,93,17,77,31,44,55,20]
 print insertionSort(arr)


if __name__ == '__main__': 
	test1() 