class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)<2:
            return False
        stack=[]
        for char in s:
            if char in "{[(":
                stack.append(char)
            else:
                if len(stack)==0:
                    return False
                if char in ")":
                    compare=stack.pop()
                    if compare!="(":
                        return False
                if char in "}":
                    compare=stack.pop()
                    if compare!="{":
                        return False
                if char in "]":
                    compare=stack.pop()
                    if compare!="[":
                        return False        
        return not stack