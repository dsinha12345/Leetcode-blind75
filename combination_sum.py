class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def helper(i,arr:List[int],total:int):
            if total == target:
                res.append(arr[:])
                return
            if total>target or i>len(candidates)-1:
                return
            arr.append(candidates[i])
            helper(i,arr,total+candidates[i])
            arr.pop()
            helper(i+1,arr,total)
        helper(0,[],0)
        return res
