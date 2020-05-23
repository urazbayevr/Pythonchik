import collections

class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # build hash map : character and how often it appears
        count = collections.Counter(s)
        print(count)
        # find the index
        for idx, ch in enumerate(s):
            #print(idx)
            if count[ch] == 1:
                print(ch)
                return idx
        return -1

s = Solution()
print(s.firstUniqChar('leetcodel'))