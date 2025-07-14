class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # hash = {}
        # for i,enum in enumerate(nums):
        #     if enum in hash:
        #         return True
        #     hash[enum] = i
        # return False
        nums_set = set(nums)
        if len(nums_set)!=len(nums):
            return True
        return False
#two methods
