class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        maps = {i:[] for i in range(numCourses)}
        for i, j in prerequisites:
            maps[i].append(j)
        
        visited = set()

        def check(course):
            if course in visited:
                return False
            if maps[course]==[]:
                return True
            visited.add(course)
            for c in maps[course]:
                if not check(c):
                    return False
            visited.remove(course)
            maps[course]= []
            return True


        for i in range(numCourses):
            if not check(i):
                return False
        return True
