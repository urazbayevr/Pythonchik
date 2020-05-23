class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a = nums.split(",")
        poryadok = sorted(a)
        counter = 0
        v = {}
        for i in poryadok:
            for j in poryadok:
                if i > j:
                    
                   counter += 1
        print(counter)


s = Solution()
print(s.smallerNumbersThanCurrent("8,1,2,2,3"))

