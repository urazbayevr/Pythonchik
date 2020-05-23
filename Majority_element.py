import collections

class Solution:
    def majorityElement(self, nums):
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)


s = Solution()
list1 = [1, 2, 3, 3, 4, 2, 2, 3]
print(s.majorityElement(list1))

