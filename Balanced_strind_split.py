import collections

class Solution(object):
    def balancedStringSplit(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = collections.Counter(s)
        print(count)

        l = 0
        r = 0
        counter = 0
        for i in range(len(s)):
            if s[i] == "L":
                l += 1
                r -= 1
            else:
                l -= 1
                r += 1
            if ((l and r) == 0):
                counter += 1
        return counter


s = Solution()
print(s.balancedStringSplit("RLRRRLLRLL"))