class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] #stack to store opening brackets
        closeopen = { ")" : "(", "]" : "[", "}" : "{"} #matcher checker

        for c in s: #for char in string
            if c in closeopen: #if char in matcher checker
                if stack and stack[-1] == closeopen[c]: #check if the stack is not empty (stack and stack[-1]) and top matches corresponding open bracket (closeopen[c])
                    stack.pop() #pop the stack
                else:
                    return False
            else:
                stack.append(c) #append char onto stack


        return True if not stack else False #if stack is empty return true, otherwise return false
        