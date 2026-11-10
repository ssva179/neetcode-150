#topological sort? -> possible try to solve it this way
#example:
#p = [[0,1],[0,2],[1,3],[1,4],[3,4]]
# 0 | [1, 2]
# 1 | [4, 3]
# 2 | []
# 3 | [4]
# 4 | []

#pseudocode:
#create hashset with nodes and all of prereqs
#use dfs to traverse down until we get to a node with no prereqs  then we can recurse back up marking each node as "complete" if we dont see it twice within that path

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #create hashset with nodes and all prereqs
        dictionary = {}
        for i in range(numCourses):
            dictionary[i] = []
        for p in prerequisites:
            dictionary[p[0]].append(p[1])

        visited = set()

        def dfs(course):
            if course in visited:
                return False
            #means no prereqs remaining, we dont add to visited
            if len(dictionary[course]) == 0:
                return True
            visited.add(course)
            for p in dictionary[course]:
                if not dfs(p):
                    return False
            #has gotten to the bottom so we can remove
            visited.remove(course)
            dictionary[course] = []
            return True
        for c in range(len(dictionary)):
            if not dfs(c):
                return False
        return True
            

        
            




        
        
