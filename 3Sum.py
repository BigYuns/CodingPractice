"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

Good Test Cases:
[]
[-1]
[0,0,0]
[-1,-1,-1,2,3,4]
[-2,-3,5]
array with a lot of duplicates 

"""
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if nums == None or len(nums) < 3:
            return [] 
        

        threeSum = 0
        result = []
        s = set() 
        
        #manipulate the input
        nums.sort() 

        for i in range(len(nums)):
            for j in range(i+1, len(nums)): 
                thirdNum = threeSum - (nums[i]+nums[j])
                if thirdNum in nums[j+1:len(nums)]:
                    if not ((nums[i],nums[j]) in s): 
                        result.append([nums[i],nums[j],thirdNum])
                        s.add((nums[i],nums[j]))
 
        return result 