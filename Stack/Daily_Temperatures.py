class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)
        for i in range(len(temperatures)):
            temp = temperatures[i]
            while stack and temp> stack[-1][0]:   
                currTemp = stack.pop()
                res[currTemp[1]] = i - currTemp[1]
            stack.append([temp, i])
        return res
