class Solution(object):
    def findComplement(self, num):
        i = 1
        while i <= num:
            print("some: ",i)
            i = i << 1
        return (i - 1) ^ num

s = Solution()
print(s.findComplement(5))