class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i>0 and nums[i] == nums[i-1]:
                continue
            
            ptr1,ptr2 = i+1, len(nums)-1
            while ptr1<ptr2:
                if nums[i]+nums[ptr1]+nums[ptr2] == 0:
                    res.append([nums[i],nums[ptr1],nums[ptr2]])
                    while ptr1<ptr2 and nums[ptr1] == nums[ptr1+1]:
                        ptr1+=1
                    while ptr1<ptr2 and nums[ptr2] == nums[ptr2-1]:
                        ptr2-=1
                    ptr1+=1
                    ptr2-=1
                elif nums[i]+nums[ptr1]+nums[ptr2]<0:
                    ptr1+=1
                else:
                    ptr2-=1
        return res
