class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        Result = []
        j = nums[n:]
        c = nums[:n]
        for i in range(len(nums)//2):
          Result.append(c[i])
          Result.append(j[i])
        return(Result)