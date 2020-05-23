class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        max_candy = max(candies)
        # for i in range(len(candies)):
        #     if (candies[i] + extraCandies) >= max_candy:
        #         print(True)
        #     else: print(False)
        otvet = ([True if (candies[i] + extraCandies) >= max_candy else False for i in range(len(candies))])
        return otvet

s = Solution()
candies = [2,3,5,1,3]
extraCandies = 3
print(s.kidsWithCandies(candies,extraCandies))