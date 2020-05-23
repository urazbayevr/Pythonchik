class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        target = []

        for i in range(len(nums)):
            target.insert(index[i], nums[i])
        return target


s = Solution()
num = [0,1,2,3,4]
ind = [0,1,2,2,1]
print(s.createTargetArray(num, ind))