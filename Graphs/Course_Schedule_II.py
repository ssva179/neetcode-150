#kahn's algorithm
#pseudocode:
#make adjacency list every idx == prereq at every idx we have a
# prereq -> [courses] bc a prereq comes before a course 
#make indegree list idx = course course has # of prereqs
#for every course with 0 indegree add to a queue 
#topsort = []*numCourses
#idx = 0
#while q:
    #curr = q.pop()
    #topsort[idx] = curr
    #idx +=1
    #for course in adj[curr]:
        #indegree[course] -=1
        #if indegree == 0:
            #q.append(course)
#if idx == numCourses -1:
    #return topsort
#return []
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:


        #make adjacency list every idx == prereq at every idx we have a
        # prereq -> [courses] bc a prereq comes before a course 
        #make indegree list idx = course course has # of prereqs
        indegrees = [0]*numCourses
        adj = [[] for i in range(numCourses)] 
        q = deque()
        for p in prerequisites:
            #[a, b] b is prereq of a
            indegrees[p[0]] +=1
            #prereq b comes before a
            adj[p[1]].append(p[0])
        #for every course with 0 indegree add to a queue 
        for course in range(numCourses):
            if indegrees[course] == 0:
                q.append(course)
       
        topsort = []
        idx = 0
        while q:
            #print(q)
            curr = q.pop()
            topsort.append(curr)
            idx +=1
            for course in adj[curr]:
                indegrees[course] -=1
                if indegrees[course] == 0:
                    q.append(course)
        if idx == numCourses:
            return topsort
        return []


        
