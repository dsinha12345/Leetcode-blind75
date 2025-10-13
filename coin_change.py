import math
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount ==0:
            return 0
        dp = [math.inf for _ in range(amount+1)]
        dp[0] = 0

        for i in range(len(dp)):
            for num in coins:
                if num<=i:
                    left = i - num
                    dp[i] = min(dp[left]+1,dp[i])
        if dp[-1] == math.inf:
            return -1
        else:
            return dp[-1]

#import math
#dynamic programming
