class Solution(object):
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        res = True
        for i in range(len(ransomNote)):
            if ransomNote[i] in magazine:
                magazine = magazine.replace(ransomNote[i], "", 1)
            else:
                res = False
        return res

s = Solution()
print(s.canConstruct("aa","ab"))
print(s.canConstruct("aa","aab"))
