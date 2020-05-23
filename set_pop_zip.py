class Solution(object):
    def destCity(self, paths):
        """
        :type paths: List[List[str]]
        :rtype: str
        """
        A, B = map(set, zip(*paths))
        print(A ,B)
        return (B - A).pop()

s = Solution()
paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
s.destCity(paths)