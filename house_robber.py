class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<2:
            return max(nums)
        dp = [0 for _ in range(len(nums))]
        for i in range(len(dp)):
            dp[i] = max(dp[i-1],nums[i]+dp[i-2])
        return dp[-1]
