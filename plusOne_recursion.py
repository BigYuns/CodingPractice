"""
Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.
"""
"""
Cases   
1) when the length is zero : return [1]
2) when the digit is 9 
3) when the digit is not 9. 

Big hints for the recursion: 
-> need to deal with the last digit in the list. 
-> need to apply the same process to each digit. 

Representative cases:
1) 9,9,9
2) 3,9,4,9
5) 1,2,3
"""

def plusOne(digits): 
	#base case
	if len(digits) == 0: 
		return [1]

	if digits[-1] == 9:
		digits = plusOne(digits[:-1])
		#digits.extend([0])
		digits.append(0)

	else:
		digits[-1] += 1

	return digits 

def lengthZero():
	digits = []
	assert plusOne(digits) == [1]

def roundUp1(): 
	digits = [8,9,9,9]
	assert plusOne(digits) == [9,0,0,0]

def roundUp2(): 
	digits = [8,4,9,9]
	assert plusOne(digits) == [8,5,0,0]

def roundUp3(): 
	digits = [9,9,9,9]
	assert plusOne(digits) == [1,0,0,0,0]


if __name__ == "__main__": 
	lengthZero() 
	roundUp1() 
	roundUp2()
	roundUp3()


"""
Tips: difference between append() and extend() 
append: Appends object at end.

x = [1, 2, 3]
x.append([4, 5])
print (x)
gives you: [1, 2, 3, [4, 5]]

extend: Extends list by appending elements from the iterable.

x = [1, 2, 3]
x.extend([4, 5])
print (x)
gives you: [1, 2, 3, 4, 5]
"""