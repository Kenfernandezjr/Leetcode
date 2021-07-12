class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        storeList = {}
        
        for start, end in edges:
            if str(start) not in storeList:
                storeList[str(start)] = 0
            if str(end) not in storeList:
                storeList[str(end)] = 0
            if str(end) in storeList:
                storeList[str(end)] += 1
            if str(start) in storeList:
                storeList[str(start)] += 1
        return max(storeList, key=storeList.get)