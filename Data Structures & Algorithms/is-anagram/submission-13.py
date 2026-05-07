class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        dictS={}
        for char in s:
            if char not in dictS:
                dictS[char]=0
            dictS[char]+=1
        
        #check if all the chars in t are in the hashmap i just created
        for char in t:
            #if the letter isnt in the hashmap or if there are count 0 left then not anagram
            if char not in dictS or dictS[char]==0:
                return False
            #key part of the algorithm because it decreases the count in the dictionary each time
            dictS[char]-=1
        
        #they are anagrams
        return True