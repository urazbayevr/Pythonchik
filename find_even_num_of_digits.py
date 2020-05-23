class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rtype = 0
        lll = []
        for i in range(len(nums)):
            a = nums[i]
            b = []
            while a > 0:
                b.append(a % 10)
                a = a // 10
            b = b[::-1]
            if (len(b) % 2 == 0):
                rtype += 1
        return rtype

s = Solution()
rle = [555,901,482,1771]
print(s.findNumbers(rle))