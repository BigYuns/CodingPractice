class Solution(object):
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        def bt(result,word,pos,curr,count):
            if pos==len(word):
                if count > 0: curr += str(count)
                result.append(curr)
                
            else: 
                bt(result,word,pos+1,curr,count+1)
                bt(result,word,pos+1,curr+(str(count) if count >0 else "")+word[pos],0)
        
        result = []
        bt(result,word,0, "",0)
        return result 
        