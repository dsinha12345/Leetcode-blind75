class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)-1

        for i in range(n,-1,-1):
            if i+nums[i]>=n:
                n=i
        return True if n==0 else False
