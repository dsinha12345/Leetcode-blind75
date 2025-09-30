class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        maxp = minp = res = nums[0]
        for i in nums[1:]:
            if i<0:
                maxp,minp = minp,maxp
            maxp = max(i, i*maxp)
            minp = min(i, i*minp)
            res = max(maxp,res)
        return res
#this is ai
# i would never write like this
