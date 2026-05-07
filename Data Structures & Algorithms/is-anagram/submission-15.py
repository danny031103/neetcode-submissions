class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        dictS={}
        for char in s:
            if char not in dictS:
                dictS[char]=1
            else:
                dictS[char]+=1
        
        for char in t:
            if char not in dictS or dictS[char]==0:
                return False
            dictS[char]-=1
        return True