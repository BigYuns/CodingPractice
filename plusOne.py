"""
Given a non-negative number represented as an array of digits, plus one to the number.

The digits are stored such that the most significant digit is at the head of the list.
"""

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if (digits == None):
            return None 
        
        if len(digits) == 0: 
            return [1]
        
        hi = len(digits)-1 
        if digits[hi] < 9: 
            digits[hi] = digits[hi]+1 
        else: 
            while (hi >= 0): 
                digits[hi] += 1
                if digits[hi] <= 9: 
                    break; 
                digits[hi] = 0
                hi -= 1 
  
            if hi== -1 and digits[hi+1] == 0 : 
                digits = [1]+ digits
            
        return digits