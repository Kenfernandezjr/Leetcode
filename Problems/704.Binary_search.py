class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def bin_search(low, high, arr, target):
            if low <= high:
            
                mid = (high + low)//2

                if nums[mid] < target:
                    low = mid + 1
                    return bin_search(low, high, arr, target)

                elif nums[mid] > target:
                    high = mid - 1
                    return bin_search(low, high, arr, target)

                else:
                    return mid

            return -1
        return bin_search(0, len(nums) -1, nums, target)