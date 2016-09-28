def merge(left, right):
	len1 = len(left)
	len 
def mergeSort(n, low, hi): 
	if len(n)==1: 
		return n 

	mid = (hi+low)/2

	left = mergeSort(n,low, mid-1)
	right = mergeSort(n,mid,hi)
	merge(left,right)

