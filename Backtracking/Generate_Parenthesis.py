#Idea: similar to permutatiosn where we recurse to the bottom i.e. 0 and the with 1 the only permutation is () ok then 2 we have ()() or (()) and so on so fort 3 ()()() (())() ((())) etc.
#question: how to make the parenthesis valid does similar index approach work
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack =[]
        res = []
        def dfs(opened, closed):
            if opened == closed == n:
                #got a bit stuck here
                res.append("".join(stack))
                return
            if opened < n:
                stack.append("(")
                dfs(opened+1, closed)
                stack.pop()
            if closed < opened:
                stack.append(")")
                dfs(opened, closed+1)
                stack.pop()
        dfs(0,0)
        return res
        
