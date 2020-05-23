class Solution(object):
    def numJewelsInStones(self, J, S):
    jwl = []
    stn = []

    for i in range(0, len(J)):
        jwl.append(J[i])
    for i in range(0, len(S)):
        stn.append(S[i])

    p = 0

    for i in range(len(stn)):
        for j in range(len(jwl)):
            if (stn[i] == jwl[j]):
                p += 1

    return p