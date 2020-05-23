class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        stack = []
        """
        for j in range(len(target)):
            for i in range(1, n+1):
                if i in target:
                    print(target[j])
                    stack.append("Push")
                elif i < target [j]:
                    print("Pop", i)
                    stack.append("Pop")
                else:
                    break
        """
        m = target[-1]
        print(m)
        for i in range(1, n+1):
            if i in target:
                print("push", i)
                stack.append("Push")
            else:
                birdeme = ["Push", "Pop"]
                stack.extend(birdeme)
                print("Pop", i)
            if i == m:
                return stack
        return stack


s = Solution()
targets = [1,2]
print(s.buildArray(targets, 4))