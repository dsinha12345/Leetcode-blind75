class Solution:
    def rob(self, nums: List[int]) -> int:
        def rob(arr):
            if not arr:
                return 0
            if len(arr)<2:
                return max(arr)
            dp = [0 for _ in range(len(arr))]
            for i in range(len(arr)):
                dp[i] = max(dp[i-1],arr[i]+dp[i-2])
            return dp[-1]
        if len(nums) ==1:
                return nums[0]
        return max(rob(nums[:-1]), rob(nums[1:]))
