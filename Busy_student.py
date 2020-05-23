class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type queryTime: int
        :rtype: int
        """
        a = list(zip(startTime,endTime))
        print(a)
        number = 0
        for i in a:
            if i[0] <= queryTime and i[1] >= queryTime:
                number += 1

        return number
s = Solution()
startTime = [9,8,7,6,5,4,3,2,1]
endTime = [10,10,10,10,10,10,10,10,10]
queryTime = 5
print(s.busyStudent(startTime,endTime,queryTime))