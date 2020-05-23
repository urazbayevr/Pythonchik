class Solution:
    def decompressRLElist(self, nums):
        res = []
        for i in range(1, len(nums), 2):
            res += [nums[i]]*nums[i-1]

        
        return res

"""
class Solution:
	def decompressRLElist(self, nums: List[int]) -> List[int]:
		i = 0
		res = []
		while i < len(nums):
			res.extend(nums[i] * [nums[i + 1]])
			i += 2
		return res
"""

s = Solution()
rle = [1,2,5,4,7,3,4,2]
print(s.decompressRLElist(rle))

