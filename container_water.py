class Solution:
    def maxArea(self, height: List[int]) -> int:
        ptr1,ptr2 = 0, len(height)-1
        max_vol=0
        while ptr1<ptr2:
            max_vol = max(max_vol,(ptr2-ptr1)*min(height[ptr1],height[ptr2]))
            if height[ptr1]<height[ptr2]:
                ptr1+=1
            else:
                ptr2-=1
        return max_vol
#easiest problem hahaha
#back here again

