class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        totalTime = 0
        for i in range(len(points) - 1):
            p1 = points[i]
            p2 = points[i + 1]
            totalTime += (max(abs(p2[1] - p1[1]), abs(p2[0] - p1[0])))
        return totalTime

s = Solution()
list = [[1,1],[3,4],[-1,0]]
print(s.minTimeToVisitAllPoints(list))