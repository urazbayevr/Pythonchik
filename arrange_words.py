class Solution(object):
    def arrangeWords(self, text):
        """
        :type text: str
        :rtype: str
        """
        print(len(text))
        a = text.split()
        l = 0
        """ans = ' '.join(sorted([w.lower() for w in text.split()], key=lambda x: len(x)))
        return ans[0].upper() + ans[1:]"""

        l = text.split(" ")
        s = sorted(l, key=lambda word: len(word))
        s = " ".join(s).capitalize()

        return s


s = Solution()
text = "Leetcode is cool"
print(s.arrangeWords(text))