class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        a = "("+")"
        b = ''
        for i in range(len(S)):
            if S[i] == "(" and S[i+1] == ")":
                b += a
        return b

s = "(()())(())"
a = Solution()
print(a.removeOuterParentheses(s))