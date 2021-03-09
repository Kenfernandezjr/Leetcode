# Given Two Arrays, write a function to compute their intersection
# Each element in the result must be unique
# The result can be in any order

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        myList = []
        left = 0
        left2 = 0
        nums1.sort()
        nums2.sort()
        
        while left < len(nums1) and left2 < len(nums2):
            
            if nums1[left] == nums2[left2]:
                myList.append(nums1[left])
                left += 1
                left2 += 1
            
            elif nums1[left] < nums2[left2]:
                left += 1
                
            else:
                left2 += 1
         
        return list(set(myList))