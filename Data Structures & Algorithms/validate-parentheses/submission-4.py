class Solution:
    def isValid(self, s: str) -> bool:
        #create stack to push open into
        stack = []

        #go through array
        for x in s:
            #if its one of the open ones then push it
            if x in "([{":
                stack.append(x)

            #if not check if the top most in the stack is the counterpart, if not return false
            elif x == ")":
                if not stack or stack.pop() != "(":
                    return False
            elif x == "}":
                if not stack or stack.pop() != "{":
                    return False
            elif x == "]":
                if not stack or stack.pop() != "[":
                    return False
            #return the stack empty or not
        return not stack