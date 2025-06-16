#Not so efficient
import heapq
class MedianFinder:

    def __init__(self):
        self.data = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.data, num)

    def findMedian(self) -> float:
        temp_data = self.data.copy()
        if len(temp_data)==0:
            return None
        n=len(temp_data)
        if n%2!=0:
            med = n//2
            element = 0
            for i in range(med+1):
                element = heapq.heappop(temp_data)
            return element
        else:
            med = n//2
            element = 0
            for i in range(med):
                element = heapq.heappop(temp_data)
            next_ele = heapq.heappop(temp_data)
            return (element+next_ele)/2
