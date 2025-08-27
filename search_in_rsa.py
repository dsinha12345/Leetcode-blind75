#repeated
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def find_l(arr):
            l,h = 0, len(arr)-1

            while l<h:
                mid = l+(h-l)//2
                if arr[mid]>arr[h]:
                    l = mid +1
                else:
                    h = mid
            return l
        def binary_search(l,h,arr,element):
            while l<=h:
                mid = l+(h-l)//2
                if arr[mid] == element:
                    return mid
                elif arr[mid]>element:
                    h = mid -1
                else:
                    l = mid + 1
            return -1
        
        l_arr= find_l(nums)
        h= len(nums)-1
        if nums[l_arr]<=target<=nums[h]:
            return binary_search(l_arr,h,nums,target)
        else:
            return binary_search(0,l_arr-1,nums,target)
