"""
Given a collection of intervals, merge all overlapping intervals.

For example,
Given [1,3],[2,6],[8,10],[15,18],
return [1,6],[8,10],[15,18].

"""

class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        def getKey(interval):
            return interval.start 
            
        if len(intervals) ==0 or intervals==None: 
            return []
            
        intervals = sorted(intervals,key=getKey)
        result = []
        result.append(intervals[0])
        
        for i in range(1,len(intervals)):
            if result[len(result)-1].end < intervals[i].start: 
                result.append(Interval(intervals[i].start, intervals[i].end))

            originalStart,originalEnd  = result[len(result)-1].start , result[len(result)-1].end

            s=originalStart if originalStart < intervals[i].start else intervals[i].start
            e=originalEnd if originalEnd > intervals[i].end else intervals[i].end 
            
            result[len(result)-1].start, result[len(result)-1].end = s,e 
        
        return result 

# def test1():
# 	interval1 = Interval(1,3)
# 	intervals = [interval1]
# 	sol = Solution()
# 	print sol.merge(intervals)[0].start

# if __name__ == '__main__':
# 	test1()

"""
Time complexity: nlongn
space comlexity : n
"""

"""
key points: 
sorted return a new array while a.sorted is modifying the original array itself. 
inside function: i don't need to make getKey as an attirbute of an instance. 
In this case, getKey function should be declared beforehand. 

Type: array and sort. 
"""

"""
Shorter Example Answer: 
Just go through the intervals sorted by start coordinate and either combine the current interval with the previous one if they overlap, or add it to the output by itself if they don't.
"""


# def merge(self, intervals):
#     out = []
#     for i in sorted(intervals, key=lambda i: i.start):
#         if out and i.start <= out[-1].end:
#             out[-1].end = max(out[-1].end, i.end)
#         else:
#             out += i,
#     return out