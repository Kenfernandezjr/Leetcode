class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        list2 = []
        
        while left < right:

            if numbers[left] + numbers[right] < target:
                left = left + 1
                
            elif numbers[left] + numbers[right] > target:
                right = right - 1
                
            else:
                list2.append(left + 1) 
                list2.append(right + 1)
                return list2