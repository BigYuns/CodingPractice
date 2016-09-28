#get the first row from P =a  
        #check which row of G contains a  --> get the row number 
        #first check the # of rows from current row to remaning row = len(p ) 
            #if not, return False (or stout No)
        #i=1
        # while i+1 < r: 
            #if  p[i] in G[row+i]: 
              #i =i+1 
            #return False 
        #return True 




1
2 6
999999
121211
2 2
99
11




import sys

n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))


sum = 0
for i in range(n):
    sum += arr[i]
print sum


or 
import sys
for line in sys.stdin:
  print line

