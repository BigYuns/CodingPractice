from collections import defaultdict

class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.dict = collections.defaultdict(set)
        for w in dictionary: 
            abbr=w
            if len(w) >2: 
                abbr = w[0]+str(len(w)-2)+w[-1]
            self.dict[abbr].add(w) 

    def isUnique(self, word):
        """    ..eeee
        check if a word is unique.
        :type word: str
        :rtype: bool
        """   
        abbr = word
        if len(word) > 2: 
            abbr = word[0]+str(len(word)-2)+word[-1]
        return (abbr not in self.dict.keys()) or (len(self.dict[abbr])==1 and word ==list(self.dict[abbr])[0])


# def test1(): 
#     dictionary = ["a","a"]
#     vwa = ValidWordAbbr(dictionary)
#     print vwa.isUnique("a")  #true 
#     print vwa.isUnique("hello") #true 
                

# def test2(): 
#     dictionary = ["dog"]
#     vwa = ValidWordAbbr(dictionary)
#     print vwa.isUnique("dig")  #false 

# def test3(): 
#     dictionary = ["dog", "dog"]
#     vwa = ValidWordAbbr(dictionary)
#     print vwa.isUnique("dog")  #true 

# def test4(): 
#     dictionary = ["dog", "dig"]
#     vwa = ValidWordAbbr(dictionary)
#     print vwa.isUnique("dog")  #false

def test5(): 
    dictionary = [""]
    vwa = ValidWordAbbr(dictionary) 

    print vwa.isUnique("a")
    print vwa.isUnique("")

if __name__ == '__main__': 
    #test1()
    #test2()
    #test3()
    #test4() 
    test5() 
