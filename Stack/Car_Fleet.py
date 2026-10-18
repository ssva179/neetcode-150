#pseudocode
#add pairs of position, speend to a list sort and reverse
#iterate through the pairs
    #calculate pair time
    #append to stack
    #if time <= top of stack continue
    #else time to stack 
#return len of stack
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sort = []
        for i in range(len(position)):
            sort.append([position[i],speed[i]])
        sort.sort()
        sort.reverse()
        stack = deque()
        for pair in sort:
            t = (target-pair[0])/pair[1]
            stack.append(t)
            if len(stack) > 1:
                cur = stack.pop()
                if cur <= stack[-1]:
                    continue
                else:
                    stack.append(cur)
        return len(stack)
