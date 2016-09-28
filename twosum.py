from collections import defaultdict

class TwoSum(object):

    def __init__(self):
        """
        initialize your data structure here
        """
        self.dict = defaultdict(lambda:0)
        #self.count = 0

    def add(self, number):
        """
        Add the number to an internal data structure.
        :rtype: nothing
        """
        self.dict[number] += 1
        #self.count +=1


    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
    
        #if self.count < 2: 
            #return False 
        
        copy = self.dict

        for i in copy:
            if (value-i) in copy and (value-i !=i or copy[i] >1):
                return True 
        return False 
    
    
    
# Your TwoSum object will be instantiated and called as such:
# twoSum = TwoSum()
# twoSum.add(number)
# twoSum.find(value)