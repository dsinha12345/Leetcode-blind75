class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find_ll(arr,low=0,high=len(nums)-1):
            while low<high:
                mid = low+(high-low)//2
                if arr[mid]>arr[high]:
                    low = mid+1
                else:
                    high = mid
            return low
        
        def search_ele(arr,low,high,target):
            while low<=high:
                mid = low+(high-low)//2
                if arr[mid] ==target:
                    return mid
                elif arr[mid]<target:
                    low = mid +1 
                else:
                    high = mid-1
            return -1

        low = find_ll(nums,0,len(nums)-1)
        if low == 0:
            return search_ele(nums, 0, len(nums) - 1, target)
        if nums[0]<=target<=nums[low-1]:
            return search_ele(nums,0,low-1,target)
        else:
            return search_ele(nums,low,len(nums)-1,target)
