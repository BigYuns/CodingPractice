# Definition for singly-linked list.

#change it to the node one 

class ListNode(object):
    
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None or l2 == None:
            return None

        toss = 0 
        prevNode = ListNode(None) 
        
        return self.iteration(l1,l2,toss,prevNode)
        
    def iteration(self, l1,l2,toss,prev): 

        while l1!=None or l2 != None: 
            first_value = l1.val if l1!=None else 0 
            second_value = l2.val if l2!=None else 0 
 
            sum =first_value +second_value+toss
            val = sum%10
            toss = sum/10
            
            currentNode = ListNode(val)

            if prev.val==None: 
                head = currentNode 
            prev.next = currentNode 
            prev = currentNode 
            l1=l1.next if l1 !=None else None
            l2 =l2.next if l2 != None else None 
           

        if toss==1: 
            prev.next = ListNode(1) 
        
        return head 


"""
Key points: 
1) when l1=None vs l1 = ListNode(None) is different! 
2) when I am trying to access to the decorators of the node, make sure to check whether the node itself is None or not. 
3) Summation is always important to check whether it is greater than 9 or not. 
    -good idea to create a variable to check either the variable is one or zero. 
""""