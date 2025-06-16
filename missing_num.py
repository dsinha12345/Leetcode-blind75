class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = sum(nums)
        real = 0
        for i in range(1,len(nums)+1):
            real+=i
        return real - total
