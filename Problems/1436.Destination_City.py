class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        list1 = set([])
        list2 = set([])
         
        for start, end in paths:
            list1.add(start)
            list2.add(end)
        return list(list2.difference(list1))[0]