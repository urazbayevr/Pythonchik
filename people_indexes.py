class Solution(object):
    def peopleIndexes(self, favoriteCompanies):
        N = len(favoriteCompanies)
        sets = [set(lst) for lst in favoriteCompanies]
        print(sets)
        ans = []
        for i in range(N):
            boo = True
            for j in range(N):
                print(sets[i].issubset(sets[j]))
                if i != j and sets[i].issubset(sets[j]):
                    boo = False
            if boo:
                ans.append(i)
        return ans

s = Solution()
favoriteCompanies = [["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]]
print(s.peopleIndexes(favoriteCompanies))


"""def peopleIndexes(self, favoriteCompanies):
    
    ansll = []
    for i in range(len(favoriteCompanies)):
        set1 = set(favoriteCompanies[i])
        flag = 1
        for j in range(len(favoriteCompanies)):
            set2 = set(favoriteCompanies[j])
            comm = set1.intersection(set2)
            if (comm == set1 and i != j):
                flag = 0
        if (flag):
            ansll.append(i)
    return ansll"""