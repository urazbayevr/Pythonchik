class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(len(nums)):
            count = 0
            #print(i)
            for j in range(len(nums)):
                print(j)
                if i != j and nums[i] > nums[j]:
                    count += 1
            res.append(count)

        return res

s = Solution()
nomerlar = [8, 1, 2, 2, 3]
print(s.smallerNumbersThanCurrent(nomerlar))
"""
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        m = {}
        for i, num in enumerate(sorted(nums)):
            m.setdefault(num, i)
        return map(m.get, nums)
"""