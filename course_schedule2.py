class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        maps = {i:[] for i in range(numCourses)}
        for i,j in prerequisites:
            maps[i].append(j)
        order = []
        visited, cycle = set(), set()
        def check(course):
            if course in cycle:
                return False
            if course in visited:
                return True
            
            cycle.add(course)
            for i in maps[course]:
                if not check(i):
                    return False
            cycle.remove(course)
            visited.add(course)
            maps[course] = []
            order.append(course)
            return True

        for i in range(numCourses):
            if not check(i):
                return []
        return order
