class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in nums[len(nums)//2:]:
            if nums.count(i) > (len(nums)//2):
                return(i)
                break
            else:
                continue