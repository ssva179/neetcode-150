#pseudocode
#stack = deque()
#while starting bracket:
    #insert into stack:
#while list not empty:
    #if closing bracket does not match opening breacket 
        #return false 

class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        i = 0
        while i < len(s):
            if s[i] in "{[(":
                stack.append(s[i])
            else:
                if not stack:
                    return False
                elif stack[-1] == "[" and s[i] == "]":
                    stack.pop()
                elif stack[-1] == "{" and s[i] == "}":
                    stack.pop()
                elif stack[-1] == "(" and s[i] == ")":
                    stack.pop()
                else:
                    return False
            i+=1
        if stack:
            return False
        else:
            return True
