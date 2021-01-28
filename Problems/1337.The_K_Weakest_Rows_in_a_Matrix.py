class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        results = []
        soldiers = []
        for i in range(len(mat)):
            count = 0
            for j in range(len(mat[i])):
                if mat[i][j] is 1:
                    count += 1
            soldiers.append((count, i))
        soldiers.sort()
    
        for count,x in soldiers[:k]:
            results.append(x)
        return results