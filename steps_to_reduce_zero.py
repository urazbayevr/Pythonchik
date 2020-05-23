class Solution(object):
    def numberOfSteps(self, num):
        steps = 0
        while(num != 0):
            if (num % 2 == 0):
                num = num / 2
                print("osi joli bilari kiskaradi: ", num)
                steps = steps + 1
            else:
                num = num - 1
                print("al mina joli osilai kiskaradi", num)
                steps = steps + 1

        return steps

s = Solution()
print(s.numberOfSteps(123))